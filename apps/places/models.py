# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from apps.glue import FixedCharField, RtfTextField, VagueDateField
from apps.glue.models import RecorderBaseModel
from apps.names.models import Name
from apps.admin_areas.models import AdminArea

class LocationType(models.Model):
    location_type_key = FixedCharField(db_column='LOCATION_TYPE_KEY', primary_key=True, max_length=16)
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)
    authority = models.CharField(db_column='AUTHORITY', max_length=100, blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_TYPE'

    def __str__(self):
        return self.short_name

class Location(models.Model):
    location_key = FixedCharField(db_column='LOCATION_KEY', primary_key=True, max_length=16)
    description = RtfTextField(db_column='DESCRIPTION', blank=True, null=True)
    parent_key = models.ForeignKey('self', models.DO_NOTHING, db_column='PARENT_KEY', blank=True, null=True)
    spatial_ref = models.CharField(db_column='SPATIAL_REF', max_length=40, blank=True, null=True)
    spatial_ref_system = models.CharField(db_column='SPATIAL_REF_SYSTEM', max_length=4)
    lat = models.FloatField(db_column='LAT')
    long = models.FloatField(db_column='LONG')
    location_type_key = models.ForeignKey('LocationType', models.DO_NOTHING, db_column='LOCATION_TYPE_KEY')
    file_code = models.CharField(db_column='FILE_CODE', max_length=20, blank=True, null=True)
    spatial_ref_qualifier = models.CharField(db_column='SPATIAL_REF_QUALIFIER', max_length=20)
    approach = RtfTextField(db_column='APPROACH', blank=True, null=True)
    restriction = RtfTextField(db_column='RESTRICTION', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION'

    def __str__(self):
        for name in self.names.all():
            if name.preferred:
                return name.item_name
        return 'Unknown'

    def get_absolute_url(self):
        return f"/places/location/{self.location_key}/"


class LocationFeature(models.Model):
    location_feature_key = FixedCharField(db_column='LOCATION_FEATURE_KEY', primary_key=True, max_length=16)
    item_name = models.CharField(db_column='ITEM_NAME', max_length=60)
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='features')
    feature_grading_key = models.ForeignKey('LocationFeatureGrading', models.DO_NOTHING, db_column='FEATURE_GRADING_KEY', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_FEATURE'

    def __str__(self):
        return self.item_name


class LocationFeatureGrading(models.Model):
    feature_grading_key = FixedCharField(db_column='FEATURE_GRADING_KEY', primary_key=True, max_length=16)
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    location_feature_type_key = models.ForeignKey('LocationFeatureType', models.DO_NOTHING, db_column='LOCATION_FEATURE_TYPE_KEY')
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_FEATURE_GRADING'

    def __str__(self):
        return self.short_name


class LocationFeatureType(models.Model):
    location_feature_type_key = FixedCharField(db_column='LOCATION_FEATURE_TYPE_KEY', primary_key=True, max_length=16)
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_FEATURE_TYPE'

    def __str__(self):
        return self.short_name


class DamageOccurrence(models.Model):
    damage_occurrence_key = FixedCharField(db_column='DAMAGE_OCCURRENCE_KEY', primary_key=True, max_length=16)
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)
    vague_date_start = VagueDateField(db_column='VAGUE_DATE_START', max_length=50, blank=True, null=True)
    vague_date_end = models.IntegerField(db_column='VAGUE_DATE_END', blank=True, null=True)
    vague_date_type = models.CharField(db_column='VAGUE_DATE_TYPE', max_length=2)
    location_feature_key = models.ForeignKey('LocationFeature', models.DO_NOTHING, db_column='LOCATION_FEATURE_KEY', related_name='damage_occurrences')
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DAMAGE_OCCURRENCE'


class ThreatType(models.Model):
    threat_type_key = FixedCharField(db_column='THREAT_TYPE_KEY', primary_key=True, max_length=16)
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'THREAT_TYPE'

    def __str__(self):
        return self.short_name


class PotentialThreat(models.Model):
    potential_threat_key = FixedCharField(db_column='POTENTIAL_THREAT_KEY', primary_key=True, max_length=16)
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)
    threat = models.CharField(db_column='THREAT', max_length=60)
    threat_type_key = models.ForeignKey('ThreatType', models.DO_NOTHING, db_column='THREAT_TYPE_KEY')
    location_feature_key = models.ForeignKey(LocationFeature, models.DO_NOTHING, db_column='LOCATION_FEATURE_KEY', related_name='potential_threats')
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'POTENTIAL_THREAT'


class LocationName(models.Model):
    location_name_key = FixedCharField(db_column='LOCATION_NAME_KEY', primary_key=True, max_length=16)
    item_name = models.CharField(db_column='ITEM_NAME', max_length=100)
    preferred = models.BooleanField(db_column='PREFERRED')
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='names')
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_NAME'

class SiteStatus(models.Model):
    site_status_key = FixedCharField(db_column='SITE_STATUS_KEY', primary_key=True, max_length=16)
    short_name = models.CharField(db_column='SHORT_NAME', max_length=40)
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SITE_STATUS'

    def __str__(self):
        return self.short_name

class LocationDesignation(models.Model):
    designation_key = FixedCharField(db_column='DESIGNATION_KEY', primary_key=True, max_length=16)
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='designations')
    site_status_key = models.ForeignKey('SiteStatus', models.DO_NOTHING, db_column='SITE_STATUS_KEY')
    ref_code = models.CharField(db_column='REF_CODE', max_length=20, blank=True, null=True)
    authority = models.ForeignKey(Name, models.DO_NOTHING, db_column='AUTHORITY')
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)
    comment = RtfTextField(db_column='COMMENT', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_DESIGNATION'


class LocationAdminArea(models.Model):
    location_admin_areas_key = FixedCharField(db_column='LOCATION_ADMIN_AREAS_KEY', primary_key=True, max_length=16)
    admin_area_key = models.ForeignKey(AdminArea, models.DO_NOTHING, db_column='ADMIN_AREA_KEY')
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='admin_areas')
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_ADMIN_AREAS'


class LocationBoundary(RecorderBaseModel):
    location_boundary_key = FixedCharField(db_column='LOCATION_BOUNDARY_KEY', primary_key=True, max_length=16)
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY')
    from_vague_date_start = VagueDateField(db_column='FROM_VAGUE_DATE_START', max_length=50, blank=True, null=True)
    from_vague_date_end = models.IntegerField(db_column='FROM_VAGUE_DATE_END', blank=True, null=True)
    from_vague_date_type = models.CharField(db_column='FROM_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)
    to_vague_date_start = VagueDateField(db_column='TO_VAGUE_DATE_START', max_length=50, blank=True, null=True)
    to_vague_date_end = models.IntegerField(db_column='TO_VAGUE_DATE_END', blank=True, null=True)
    to_vague_date_type = models.CharField(db_column='TO_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)
    version = models.SmallIntegerField(db_column='VERSION')
    map_sheet_key = FixedCharField(db_column='MAP_SHEET_KEY', max_length=16, blank=True, null=True)
    object_id = models.CharField(db_column='OBJECT_ID', max_length=30, blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)
    external_filename = models.CharField(db_column='External_Filename', max_length=255, blank=True, null=True)
    external_filename_keyfield = models.CharField(db_column='External_Filename_KeyField', max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_BOUNDARY'


class LocationRelation(models.Model):
    location_relation_key = FixedCharField(db_column='LOCATION_RELATION_KEY', primary_key=True, max_length=16)
    location_key_1 = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY_1', related_name='related_locations')
    location_key_2 = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY_2')
    relationship = models.CharField(db_column='RELATIONSHIP', max_length=50)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_RELATION'


class LocationUse(RecorderBaseModel):
    location_use_key = FixedCharField(db_column='LOCATION_USE_KEY', primary_key=True, max_length=16)
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='uses')
    location_use = models.CharField(db_column='LOCATION_USE', max_length=30)
    potential = models.TextField(db_column='POTENTIAL', blank=True, null=True)
    from_vague_date_start = VagueDateField(db_column='FROM_VAGUE_DATE_START', max_length=50, blank=True, null=True)
    from_vague_date_end = models.IntegerField(db_column='FROM_VAGUE_DATE_END', blank=True, null=True)
    from_vague_date_type = models.CharField(db_column='FROM_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)
    to_vague_date_start = VagueDateField(db_column='TO_VAGUE_DATE_START', max_length=50, blank=True, null=True)
    to_vague_date_end = models.IntegerField(db_column='TO_VAGUE_DATE_END', blank=True, null=True)
    to_vague_date_type = models.CharField(db_column='TO_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LOCATION_USE'


class LandParcel(models.Model):
    land_parcel_key = FixedCharField(db_column='LAND_PARCEL_KEY', primary_key=True, max_length=16)
    location_key = models.ForeignKey('Location', models.DO_NOTHING, db_column='LOCATION_KEY', related_name='land_parcels')
    land_parcel_number = models.CharField(db_column='LAND_PARCEL_NUMBER', max_length=20)
    land_parcel_map_sheet = models.CharField(db_column='LAND_PARCEL_MAP_SHEET', max_length=30)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LAND_PARCEL'


class TenureType(models.Model):
    tenure_type_key = FixedCharField(db_column='TENURE_TYPE_KEY', primary_key=True, max_length=16)
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TENURE_TYPE'

    def __str__(self):
        return self.short_name


class Tenure(RecorderBaseModel):
    tenure_key = FixedCharField(db_column='TENURE_KEY', primary_key=True, max_length=16)
    from_vague_date_start = VagueDateField(db_column='FROM_VAGUE_DATE_START', max_length=50, blank=True, null=True)
    from_vague_date_end = models.IntegerField(db_column='FROM_VAGUE_DATE_END', blank=True, null=True)
    from_vague_date_type = models.CharField(db_column='FROM_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)
    to_vague_date_start = VagueDateField(db_column='TO_VAGUE_DATE_START', max_length=50, blank=True, null=True)
    to_vague_date_end = models.IntegerField(db_column='TO_VAGUE_DATE_END', blank=True, null=True)
    to_vague_date_type = models.CharField(db_column='TO_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)
    owned_by = models.ForeignKey(Name, models.DO_NOTHING, db_column='OWNED_BY', blank=True, null=True)
    tenure_type_key = models.ForeignKey('TenureType', models.DO_NOTHING, db_column='TENURE_TYPE_KEY', blank=True, null=True)
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', blank=True, null=True, related_name='tenures')
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TENURE'