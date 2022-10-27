from django import forms
from django.utils.translation import gettext as _
from .models import Location, LocationName, LocationDesignation
from django_select2 import forms as s2forms

LocationNameFormSet = forms.inlineformset_factory(Location, LocationName, fields=('item_name','preferred',), extra=1)

class LocationUpdateNamesForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


class LocationUpdateGeneralForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [
      'file_code',
      'location_type_key',
      'spatial_ref',
      'description',
    ]
    widgets = {
      'file_code': forms.TextInput(
        attrs = {
          'placeholder': _('Any code used to identify the location can be entered here')
        }
      ),
    }
    labels = {
      'location_type_key': _('Location type'),
    }


LocationDesignationFormSet = forms.inlineformset_factory(
    Location,
    LocationDesignation,
    fields=(
      'site_status_key',
      'ref_code',
      'authority',
      'date_from',
      'date_to',
      'comment',
    ),
    labels = {
      'site_status_key': _('Site status'),
    },
    extra=1,
  )

class LocationUpdateDesignationsForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


class LocationUpdateOtherApproachForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [
      'approach',
      'restriction',
    ]
    widgets = {
      'approach': forms.Textarea(
        attrs = {
          'placeholder': _('Describe how to get to the location')
        }
      ),
      'restriction': forms.Textarea(
        attrs = {
          'placeholder': _('Details of any access restrictions')
        }
      )
    }