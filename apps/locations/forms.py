from django import forms
from .models import Location, LocationName
from django.utils.translation import gettext as _

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
      )
    }

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
          'placeholder': _('Enter details of getting to the location')
        }
      ),
      'restriction': forms.Textarea(
        attrs = {
          'placeholder': _('Details of any access restrictions')
        }
      )
    }