from django.db import models
import datetime
import re

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
        r = re.compile('.*vague_date_start')
        field_names = [field.name for field in self._meta.get_fields()]
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
                    print('matches')
                    print (matches)
                    if matches:
                      print (matches.group(1))
                      date = datetime.datetime.fromisoformat(matches.group(3) + '-' + matches.group(2) + '-' + matches.group(1))
                      setattr(self, start_field, int(date.timestamp() / (24 * 60 * 60) + self.DAYS_ADJUST + 1))
                      setattr(self, prefix + 'vague_date_end', int(date.timestamp() / (24 * 60 * 60) + self.DAYS_ADJUST + 1))
                      setattr(self, prefix + 'vague_date_type', 'D')

        super().save(*args, **kwargs)