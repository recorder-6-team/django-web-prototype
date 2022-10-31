from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from apps.glue import FixedCharField

class R6UserManager(BaseUserManager):
    use_in_migrations = True

    # python manage.py createsuperuser
    def create_superuser(self, username, password):
        # TODO: Needs implementation
        user = self.model(
                          username = username,
                          password = password,
                          )
        user.save(using=self._db)
        return user

class Name(models.Model):
    name_key = FixedCharField(db_column='NAME_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    organisation = models.BooleanField(db_column='ORGANISATION')  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = FixedCharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NAME'

    def __str__(self):
        if self.organisation:
          return self.organisation_fields.full_name
        else:
          if self.individual_fields.forename:
            return self.individual_fields.forename + ' ' + self.individual_fields.surname
          else:
            return self.individual_fields.surname

class Individual(models.Model):
    name_key = models.OneToOneField('Name', models.DO_NOTHING, db_column='NAME_KEY', primary_key=True, related_name='individual_fields')  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    forename = models.CharField(db_column='FORENAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    initials = FixedCharField(db_column='INITIALS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    honorifics = models.CharField(db_column='HONORIFICS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    surname = models.CharField(db_column='SURNAME', max_length=30)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    born_vague_date_start = models.IntegerField(db_column='BORN_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    born_vague_date_end = models.IntegerField(db_column='BORN_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    born_vague_date_type = models.CharField(db_column='BORN_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    died_vague_date_start = models.IntegerField(db_column='DIED_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    died_vague_date_end = models.IntegerField(db_column='DIED_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    died_vague_date_type = models.CharField(db_column='DIED_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    person_floreat = models.CharField(db_column='PERSON_FLOREAT', max_length=12, blank=True, null=True)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    organisation_department_key = models.ForeignKey('OrganisationDepartment', models.DO_NOTHING, db_column='ORGANISATION_DEPARTMENT_KEY', blank=True, null=True)  # Field name made lowercase.
    active_vague_date_start = models.IntegerField(db_column='ACTIVE_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    active_vague_date_end = models.IntegerField(db_column='ACTIVE_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    active_vague_date_type = models.CharField(db_column='ACTIVE_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INDIVIDUAL'


class Organisation(models.Model):
    name_key = models.OneToOneField(Name, models.DO_NOTHING, db_column='NAME_KEY', primary_key=True, related_name='organisation_fields')  # Field name made lowercase.
    full_name = models.CharField(db_column='FULL_NAME', max_length=60)  # Field name made lowercase.
    acronym = models.CharField(db_column='ACRONYM', max_length=10, blank=True, null=True)  # Field name made lowercase.
    founded_vague_date_start = models.IntegerField(db_column='FOUNDED_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    founded_vague_date_end = models.IntegerField(db_column='FOUNDED_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    founded_vague_date_type = models.CharField(db_column='FOUNDED_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ended_vague_date_start = models.IntegerField(db_column='ENDED_VAGUE_DATE_START', blank=True, null=True)  # Field name made lowercase.
    ended_vague_date_end = models.IntegerField(db_column='ENDED_VAGUE_DATE_END', blank=True, null=True)  # Field name made lowercase.
    ended_vague_date_type = models.CharField(db_column='ENDED_VAGUE_DATE_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    comment = models.TextField(db_column='COMMENT', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    organisation_type_key = models.ForeignKey('OrganisationType', models.DO_NOTHING, db_column='ORGANISATION_TYPE_KEY', blank=True, null=True)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORGANISATION'


class OrganisationDepartment(models.Model):
    organisation_department_key = FixedCharField(db_column='Organisation_Department_Key', primary_key=True, max_length=16)  # Field name made lowercase.
    name_key = models.ForeignKey(Organisation, models.DO_NOTHING, db_column='Name_Key')  # Field name made lowercase.
    acronym = models.CharField(db_column='Acronym', max_length=20, blank=True, null=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='Item_Name', max_length=100)  # Field name made lowercase.
    entered_by = FixedCharField(db_column='Entered_By', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='Entry_Date')  # Field name made lowercase.
    changed_by = FixedCharField(db_column='Changed_By', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='Changed_Date', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='System_Supplied_Data')  # Field name made lowercase.
    custodian = FixedCharField(db_column='Custodian', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organisation_Department'


class OrganisationType(models.Model):
    organisation_type_key = FixedCharField(db_column='ORGANISATION_TYPE_KEY', primary_key=True, max_length=16)  # Field name made lowercase.
    short_name = models.CharField(db_column='SHORT_NAME', max_length=20)  # Field name made lowercase.
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
        db_table = 'ORGANISATION_TYPE'


class User(AbstractBaseUser, PermissionsMixin):
    name_key = models.OneToOneField(Name, models.DO_NOTHING, db_column='NAME_KEY', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=20)  # Field name made lowercase.
    security_level = models.SmallIntegerField(db_column='SECURITY_LEVEL')  # Field name made lowercase.
    first_login = models.BooleanField(db_column='FIRST_LOGIN')  # Field name made lowercase.
    full_edit_own_data = models.BooleanField(db_column='FULL_EDIT_OWN_DATA')  # Field name made lowercase.
    last_login = models.DateTimeField(db_column='Django_LAST_LOGIN')  # Field name made lowercase.
    username = models.CharField(db_column='Django_USERNAME', max_length=61, unique=True)  # Field name made lowercase. Calculated by view.

    objects = R6UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    @property
    def is_superuser(self):
        return self.security_level >= 5

    @property
    def is_staff(self):
        return self.security_level >= 4

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    # Unhashed password check
    def check_password(self, raw_password):
        return self.password == raw_password

    class Meta:
        managed = False
        # Use view to obtain calculated username.
        db_table = 'USER'
        unique_together = (('name_key', 'name_key'),)