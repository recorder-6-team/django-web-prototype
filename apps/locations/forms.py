from django import forms
from .models import Location, LocationName

LocationNameFormSet = forms.inlineformset_factory(Location, LocationName, fields=('item_name','preferred',), extra=1)

class LocationUpdateForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [
      'description',
      'spatial_ref',
      'file_code',
      'approach',
      'restriction',
    ]