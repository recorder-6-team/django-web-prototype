from django.db import models
from apps.glue import FixedCharField

class Source(models.Model):
    source_key = FixedCharField(db_column='SOURCE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    internal = models.BooleanField(db_column='INTERNAL')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOURCE'


class SourceFile(models.Model):
    source_key = models.OneToOneField(Source, models.DO_NOTHING, db_column='SOURCE_KEY', primary_key=True)  # Field name made lowercase.
    file_name = models.CharField(db_column='FILE_NAME', max_length=255)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOURCE_FILE'


class Journal(models.Model):
    journal_key = FixedCharField(db_column='JOURNAL_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
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
        db_table = 'JOURNAL'


class Reference(models.Model):
    source_key = models.OneToOneField('Source', models.DO_NOTHING, db_column='SOURCE_KEY', primary_key=True)  # Field name made lowercase.
    year_vague_date_start = models.IntegerField(db_column='YEAR_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    year_vague_date_end = models.IntegerField(db_column='YEAR_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    year_vague_date_type = models.CharField(db_column='YEAR_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    full_reference = models.TextField(db_column='FULL_REFERENCE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    title = models.TextField(db_column='TITLE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.CharField(db_column='VOLUME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    part = models.SmallIntegerField(db_column='PART', blank=True, null=True)  # Field name made lowercase.
    number = models.SmallIntegerField(db_column='NUMBER', blank=True, null=True)  # Field name made lowercase.
    pages = models.CharField(db_column='PAGES', max_length=20, blank=True, null=True)  # Field name made lowercase.
    supplement = models.CharField(db_column='SUPPLEMENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='EDITION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    symposium_title = models.CharField(db_column='SYMPOSIUM_TITLE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    place_of_publication = models.CharField(db_column='PLACE_OF_PUBLICATION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reference_type = models.CharField(db_column='REFERENCE_TYPE', max_length=25)  # Field name made lowercase.
    journal_key = models.ForeignKey(Journal, models.DO_NOTHING, db_column='JOURNAL_KEY', blank=True, null=True)  # Field name made lowercase.
    original_file = models.TextField(db_column='ORIGINAL_FILE', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    physical_location = models.CharField(db_column='PHYSICAL_LOCATION', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REFERENCE'


class ReferenceAuthor(models.Model):
    author_key = FixedCharField(db_column='AUTHOR_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    initials = FixedCharField(db_column='INITIALS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=50)  # Field name made lowercase.
    source_key = models.ForeignKey(Reference, models.DO_NOTHING, db_column='SOURCE_KEY')  # Field name made lowercase.
    sort_order = models.SmallIntegerField(db_column='SORT_ORDER')  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REFERENCE_AUTHOR'


class ReferenceEditor(models.Model):
    editor_key = FixedCharField(db_column='EDITOR_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    initials = FixedCharField(db_column='INITIALS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=50)  # Field name made lowercase.
    source_key = models.ForeignKey(Reference, models.DO_NOTHING, db_column='SOURCE_KEY')  # Field name made lowercase.
    sort_order = models.SmallIntegerField(db_column='SORT_ORDER')  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REFERENCE_EDITOR'


class ReferenceNumber(models.Model):
    number_key = FixedCharField(db_column='NUMBER_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    number = models.CharField(db_column='NUMBER', max_length=20)  # Field name made lowercase.
    source_key = models.ForeignKey(Reference, models.DO_NOTHING, db_column='SOURCE_KEY')  # Field name made lowercase.
    reference_number_type = models.CharField(db_column='REFERENCE_NUMBER_TYPE', max_length=20)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REFERENCE_NUMBER'