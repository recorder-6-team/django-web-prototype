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
    entered_by = models.CharField(db_column='ENTERED_BY', max_length=16)  # Field name made lowercase.
    entry_date = models.DateTimeField(db_column='ENTRY_DATE')  # Field name made lowercase.
    changed_by = models.CharField(db_column='CHANGED_BY', max_length=16, blank=True, null=True)  # Field name made lowercase.
    changed_date = models.DateTimeField(db_column='CHANGED_DATE', blank=True, null=True)  # Field name made lowercase.
    system_supplied_data = models.BooleanField(db_column='SYSTEM_SUPPLIED_DATA')  # Field name made lowercase.
    custodian = models.CharField(db_column='CUSTODIAN', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NAME'

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

    is_superuser = True
    is_staff = True

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