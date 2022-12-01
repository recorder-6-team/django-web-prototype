"""
In relation to the OSGB conversion code,
adapted from https://pypi.org/project/OSGridConverter/

Copyright 2017 Julian Porter, JP Embedded Solutions Limited

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from django.db import models
import datetime
import re
import logging
from pyproj import Transformer

logger = logging.getLogger(__name__)

class RecorderBaseModel(models.Model):

    class Meta:
        abstract=True

    # days between Unix epoch 01/01/1970 and Recorder's zero date, which is 30/12/1899.
    DAYS_ADJUST = 25569

    # On load from db, format vague date start fields to contain the text representation of dates.
    # TODO currently only supports 'D' format (single date) and 'Y' format (single year).
    @classmethod
    def from_db(cls, db, field_names, values):
        r = re.compile('.*vague_date_start')
        date_start_fields = list(filter(r.match, field_names))
        if (len(date_start_fields)>0):
            field_values = dict(zip(field_names, values))
            for start_field in date_start_fields:
                prefix = start_field.replace('vague_date_start', '')
                start = field_values[start_field]
                end = field_values[prefix + 'vague_date_end']
                type = field_values[prefix + 'vague_date_type']
                if start != None and type == 'D':
                    date = datetime.datetime.fromtimestamp((int(start) - cls.DAYS_ADJUST) * 24 * 60 * 60)
                    start_field_index = field_names.index(start_field)
                    values[start_field_index] = date.strftime('%d/%m/%Y')
                elif start != None and type == 'Y':
                    date = datetime.datetime.fromtimestamp((int(start) - cls.DAYS_ADJUST) * 24 * 60 * 60)
                    start_field_index = field_names.index(start_field)
                    values[start_field_index] = date.strftime('%Y')

        return super().from_db(db, field_names, values)

    # Override save method to convert vague date text representations back to database values.
    def save(self, *args, **kwargs):
        field_names = [field.name for field in self._meta.get_fields()]
        r = re.compile('.*vague_date_start')
        date_start_fields = list(filter(r.match, field_names))
        if (len(date_start_fields)>0):
            for start_field in date_start_fields:
                prefix = start_field.replace('vague_date_start', '')
                date_string = getattr(self, start_field)
                if date_string:
                  year_regex = re.compile('^\d{4}$')
                  matches = year_regex.search(date_string)
                  if matches:
                    date_start = datetime.datetime.fromisoformat(date_string + '-01-01')
                    date_end = datetime.datetime.fromisoformat(date_string + '-12-31')
                    setattr(self, start_field, int(date_start.timestamp() / (24 * 60 * 60) + self.DAYS_ADJUST))
                    setattr(self, prefix + 'vague_date_end', int(date_end.timestamp() / (24 * 60 * 60) + self.DAYS_ADJUST))
                    setattr(self, prefix + 'vague_date_type', 'Y')
                  else:
                    date_regex = re.compile('^(\d{2})/(\d{2})/(\d{4})$')
                    matches = date_regex.search(date_string)
                    if matches:
                      print (matches.group(1))
                      date = datetime.datetime.fromisoformat(matches.group(3) + '-' + matches.group(2) + '-' + matches.group(1))
                      setattr(self, start_field, int(date.timestamp() / (24 * 60 * 60) + self.DAYS_ADJUST + 1))
                      setattr(self, prefix + 'vague_date_end', int(date.timestamp() / (24 * 60 * 60) + self.DAYS_ADJUST + 1))
                      setattr(self, prefix + 'vague_date_type', 'D')

        self.updateLatLongs(field_names)
        super().save(*args, **kwargs)

    # Function to use a saved OSGB grid reference to populate the lat long fields.
    def updateLatLongs(self, field_names):
        r = re.compile('^(lat|long|spatial_ref|spatial_ref_system)$')
        geo_fields = list(filter(r.match, field_names))
        if len(geo_fields) == 4:
            if getattr(self, 'spatial_ref_system').upper() == 'OSGB':
                # Clean up the sref.
                sref = getattr(self, 'spatial_ref').replace(' ', '').upper()
                match = re.match('^([A-Z]{2})(?:([0-9]+)([A-N]|[P-Z])?)?$', sref)
                if not match:
                    logger.warning('OSGB grid reference not in an expected format.')
                    return
                # Save cleaned sref.
                setattr(self, 'spatial_ref_system', 'OSGB')
                setattr(self, 'spatial_ref', sref)
                # Now work out the lat long values.
                g=match.groups()

                # First parse the 100km grid square.
                alpha=g[0]
                l1 = ord(alpha[0]) - ord('A')
                l2 = ord(alpha[1]) - ord('A')
                if l1 > 7 : l1-=1
                if l2 > 7 : l2-=1
                e100km = ((l1-2)%5)*5 +  (l2%5)
                n100km = 19-5*(l1//5) - l2//5
                if e100km<0 or e100km>6 or n100km<0 or n100km>12:
                    logger.error("Invalid grid reference: e100k = %s, n100k =%s} - OOR",e100km,n100km)
                    return

                factor = pow(10, 5)
                parsed = [e100km * factor, n100km * factor]
                # Now parse the easting/northing
                if g[1] != None:
                    c = len(g[1]) // 2
                    en = [g[1][:c], g[1][c:]]
                    if len(en[0]) != len(en[1]):
                        logger.error('Invalid grid reference: e=*%s* n=*%s* - unequal lengths',*en)
                        return

                    # Pad en so always in metres.
                    en = [int((x+'00000')[:5]) for x in en]
                    logger.warning('EN is %s',en)
                    parsed[0] = parsed[0] + en[0]
                    parsed[1] = parsed[1] + en[1]

                    # Now parse DINTY tetrad if provided.
                    if g[2] != None:
                        # Tetrads should only have a pair of single numerics.
                        if c != 1:
                            logger.error('Invalid grid reference: not a valid Tetrad')
                            return
                        dinty = ord(g[2]) - ord('A')
                        if dinty > ord('O') - ord('A'):
                          dinty = dinty - 1
                        parsed[0] = parsed[0] + (dinty // 5) * 2000
                        parsed[1] = parsed[1] + (dinty % 5) * 2000

                # Convert from OSGB1936 to WGS84.
                transformer = Transformer.from_crs(27700, 4326)
                latLon = transformer.transform(parsed[0], parsed[1])

                # Save to the database.
                setattr(self, 'lat', latLon[0])
                setattr(self, 'long', latLon[1])

            else:
                logger.warning('Transformation of non-OSGB data not yet supported.')

