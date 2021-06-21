from django.db import models
from striprtf.striprtf import rtf_to_text

class FixedCharField(models.CharField):
    description = 'A custom field for fixed char datatype fields.'

    def db_type(self, connection):
        return 'char({length})'.format(length = self.max_length)

class RtfTextField(models.TextField):
    description = 'A variant of TextField which parses RTF to plaintext when read from the database.'

    def from_db_value(self, value, expression, connection):
        if value != None:
          return rtf_to_text(value).strip()
        return value
