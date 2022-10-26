from django.db import models
from apps.glue import FixedCharField
from apps.sources.models import Source

class AdminType(models.Model):
    admin_type_key = FixedCharField(db_column='ADMIN_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=50)  # Field name made lowercase.
    long_name = models.CharField(db_column='LONG_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    authority = models.CharField(db_column='AUTHORITY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN_TYPE'


class AdminArea(models.Model):
    admin_area_key = FixedCharField(db_column='ADMIN_AREA_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=60)  # Field name made lowercase.
    admin_type_key = models.ForeignKey('AdminType', models.DO_NOTHING, db_column='ADMIN_TYPE_KEY')  # Field name made lowercase.
    parent = FixedCharField(db_column='PARENT', max_length=16, blank=True, null=True)  # Field name made lowercase.
    short_code = models.CharField(db_column='SHORT_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN_AREA'


class AdminAreaSources(models.Model):
    source_link_key = FixedCharField(db_column='SOURCE_LINK_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    admin_area_key = models.ForeignKey(AdminArea, models.DO_NOTHING, db_column='ADMIN_AREA_KEY')  # Field name made lowercase.
    source_key = models.ForeignKey(Source, models.DO_NOTHING, db_column='SOURCE_KEY')  # Field name made lowercase.
    original = models.BooleanField(db_column='ORIGINAL')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN_AREA_SOURCES'


class AdminBoundary(models.Model):
    admin_boundary_key = FixedCharField(db_column='ADMIN_BOUNDARY_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    object_id = models.SmallIntegerField(db_column='OBJECT_ID', blank=True, null=True)  # Field name made lowercase.
    authority = models.CharField(db_column='AUTHORITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    admin_area_key = models.ForeignKey(AdminArea, models.DO_NOTHING, db_column='ADMIN_AREA_KEY')  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    map_sheet_key = FixedCharField(db_column='MAP_SHEET_KEY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN_BOUNDARY'


# TODO fix reverse accessor problem with
class AdminRelation(models.Model):
    admin_relation_key = FixedCharField(db_column='ADMIN_RELATION_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    admin_area_key_1 = models.ForeignKey(AdminArea, models.DO_NOTHING, db_column='ADMIN_AREA_KEY_1', related_name='admin_area_1')  # Field name made lowercase.
    admin_area_key_2 = models.ForeignKey(AdminArea, models.DO_NOTHING, db_column='ADMIN_AREA_KEY_2', related_name='admin_area_2')  # Field name made lowercase.
    relation_1_to_2 = models.CharField(db_column='RELATION_1_TO_2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    relation_2_to_1 = models.CharField(db_column='RELATION_2_TO_1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ADMIN_RELATION'