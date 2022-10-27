from django import forms
from django.utils.translation import gettext as _
from .models import Location, LocationName, LocationDesignation, LocationAdminAreas
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


##########################
# Geo info - admin areas #
##########################

# Select2 lookup widget for admin areas.
class AdminAreasWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "item_name__icontains",
    ]

# Formset factory for admin areas.
LocationGeoInfoAdminAreaFormSet = forms.inlineformset_factory(
  Location,
  LocationAdminAreas,
  fields = ('admin_area_key',),
  widgets = {
    'admin_area_key': AdminAreasWidget,
  },
  labels = {
    'admin_area_key': _('Administrative areas'),
  },
  extra=1
)

# Form class for the list wrapper.
class LocationUpdateGeoInfoAdminAreasForm(forms.ModelForm):
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