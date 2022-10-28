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
    location_type_key = FixedCharField(db_column='LOCATION_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    authority = models.CharField(db_column='AUTHORITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION_TYPE'

    def __str__(self):
        return self.short_name

class Location(models.Model):
    location_key = FixedCharField(db_column='LOCATION_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    description = RtfTextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    parent_key = models.ForeignKey('self', models.DO_NOTHING, db_column='PARENT_KEY', blank=True, null=True)  # Field name made lowercase.
    spatial_ref = models.CharField(db_column='SPATIAL_REF', max_length=40, blank=True, null=True)  # Field name made lowercase.
    spatial_ref_system = models.CharField(db_column='SPATIAL_REF_SYSTEM', max_length=4)  # Field name made lowercase.
    lat = models.FloatField(db_column='LAT')  # Field name made lowercase.
    long = models.FloatField(db_column='LONG')  # Field name made lowercase.
    location_type_key = models.ForeignKey('LocationType', models.DO_NOTHING, db_column='LOCATION_TYPE_KEY')  # Field name made lowercase.
    file_code = models.CharField(db_column='FILE_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spatial_ref_qualifier = models.CharField(db_column='SPATIAL_REF_QUALIFIER', max_length=20)  # Field name made lowercase.
    approach = RtfTextField(db_column='APPROACH', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    restriction = RtfTextField(db_column='RESTRICTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION'

    def __str__(self):
        for name in self.names.all():
            if name.preferred:
                return name.item_name
        return 'Unknown'

    def get_absolute_url(self):
        return f"/locations/{self.location_key}/"

class LocationName(models.Model):
    location_name_key = FixedCharField(db_column='LOCATION_NAME_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=100)  # Field name made lowercase.
    preferred = models.BooleanField(db_column='PREFERRED')  # Field name made lowercase.
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='names')  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION_NAME'

class SiteStatus(models.Model):
    site_status_key = FixedCharField(db_column='SITE_STATUS_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=40)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SITE_STATUS'

    def __str__(self):
        return self.short_name

class LocationDesignation(models.Model):
    designation_key = FixedCharField(db_column='DESIGNATION_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='designations')  # Field name made lowercase.
    site_status_key = models.ForeignKey('SiteStatus', models.DO_NOTHING, db_column='SITE_STATUS_KEY')  # Field name made lowercase.
    ref_code = models.CharField(db_column='REF_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    authority = models.ForeignKey(Name, models.DO_NOTHING, db_column='AUTHORITY')  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    comment = RtfTextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION_DESIGNATION'


class LocationAdminAreas(models.Model):
    location_admin_areas_key = FixedCharField(db_column='LOCATION_ADMIN_AREAS_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    admin_area_key = models.ForeignKey(AdminArea, models.DO_NOTHING, db_column='ADMIN_AREA_KEY')  # Field name made lowercase.
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='location_admin_areas')  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION_ADMIN_AREAS'


class LocationBoundary(RecorderBaseModel):
    location_boundary_key = FixedCharField(db_column='LOCATION_BOUNDARY_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY')  # Field name made lowercase.
    from_vague_date_start = VagueDateField(db_column='FROM_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    from_vague_date_end = models.IntegerField(db_column='FROM_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    from_vague_date_type = models.CharField(db_column='FROM_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    to_vague_date_start = VagueDateField(db_column='TO_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    to_vague_date_end = models.IntegerField(db_column='TO_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    to_vague_date_type = models.CharField(db_column='TO_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    version = models.SmallIntegerField(db_column='VERSION')  # Field name made lowercase.
    map_sheet_key = FixedCharField(db_column='MAP_SHEET_KEY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    object_id = models.CharField(db_column='OBJECT_ID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    external_filename = models.CharField(db_column='External_Filename', max_length=255, blank=True, null=True)  # Field name made lowercase.
    external_filename_keyfield = models.CharField(db_column='External_Filename_KeyField', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION_BOUNDARY'


class LocationUse(RecorderBaseModel):
    location_use_key = FixedCharField(db_column='LOCATION_USE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    location_key = models.ForeignKey(Location, models.DO_NOTHING, db_column='LOCATION_KEY', related_name='uses')  # Field name made lowercase.
    location_use = models.CharField(db_column='LOCATION_USE', max_length=30)  # Field name made lowercase.
    potential = models.TextField(db_column='POTENTIAL', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    from_vague_date_start = VagueDateField(db_column='FROM_VAGUE_DATE_START', max_length=50, blank=True, null=True)  # Field name made lowercase.
    from_vague_date_end = models.IntegerField(db_column='FROM_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    from_vague_date_type = models.CharField(db_column='FROM_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    to_vague_date_start = VagueDateField(db_column='TO_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    to_vague_date_end = models.IntegerField(db_column='TO_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    to_vague_date_type = models.CharField(db_column='TO_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOCATION_USE'