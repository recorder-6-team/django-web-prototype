from django import forms
from django.utils.translation import gettext as _
from .models import LandParcel
from .models import Location
from .models import LocationAdminArea
from .models import LocationDesignation
from .models import LocationName
from .models import LocationRelation
from .models import Tenure
from .models import LocationUse
from django_select2 import forms as s2forms

####################################
# Re-usable Select2 search widgets #
####################################

class NamesWidget(s2forms.ModelSelect2Widget):
    search_fields = [
      'individual_fields__surname__icontains',
      'individual_fields__forename__icontains',
      'organisation_fields__full_name__icontains',
      'organisation_fields__acronym__icontains'
    ]

#########
# Names #
#########

LocationNamesFormSet = forms.inlineformset_factory(Location, LocationName, fields=('item_name','preferred',), extra=1)

class LocationUpdateNamesContainerForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


###########
# General #
###########

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


################
# Designations #
################

LocationDesignationsFormSet = forms.inlineformset_factory(
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
    widgets = {
      'authority': NamesWidget,
    },
    extra=1,
  )

class LocationUpdateDesignationsContainerForm(forms.ModelForm):
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
LocationGeoInfoAdminAreasFormSet = forms.inlineformset_factory(
  Location,
  LocationAdminArea,
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
class LocationUpdateGeoInfoAdminAreasContainerForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


###########################
# Geo info - land parcels #
###########################

# Formset factory for land parcels.
LocationGeoInfoLandParcelsFormSet = forms.inlineformset_factory(
  Location,
  LandParcel,
  fields = (
    'land_parcel_number',
    'land_parcel_map_sheet',
  ),
  labels = {
    'land_parcel_number': _('Number'),
    'land_parcel_map_sheet': _('Map system'),
  },
  extra=1
)

# Form class for the list wrapper.
class LocationUpdateGeoInfoLandParcelsContainerForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


#####################
# Other - relations #
#####################

# Formset factory for admin areas.
LocationOtherRelationsFormSet = forms.inlineformset_factory(
  Location,
  LocationRelation,
  fields = (
    'location_key_2',
    'relationship',
  ),
  labels = {
    'location_2': _('Related location'),
  },
  fk_name = 'location_key_1',
  extra=1

)

# Form class for the list wrapper.
class LocationUpdateOtherRelationsContainerForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


################
# Other - uses #
################

# Formset factory for admin areas.
LocationOtherUsesFormSet = forms.inlineformset_factory(
  Location,
  LocationUse,
  fields = (
    'location_use',
    'potential',
    'from_vague_date_start',
    'to_vague_date_start',
    'comment',
  ),
  labels = {
    'location_use': _('Use'),
    'from_vague_date_start': _('From'),
    'to_vague_date_start': _('To'),
    'comment': _('Comments'),
  },
  extra=1
)

# Form class for the list wrapper.
class LocationUpdateOtherUsesContainerForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


##################
# Other - tenure #
##################

# Formset factory for tenure.
LocationOtherTenuresFormSet = forms.inlineformset_factory(
  Location,
  Tenure,
  fields = (
    'owned_by',
    'tenure_type_key',
    'from_vague_date_start',
    'to_vague_date_start',
  ),
  labels = {
    'owned_by': _('Owner'),
    'from_vague_date_start': _('From'),
    'to_vague_date_start': _('To'),
    'tenure_type_key': _('Type'),
  },
  widgets = {
    'owned_by': NamesWidget,
  },
  extra=1
)

# Form class for the list wrapper.
class LocationUpdateOtherTenuresContainerForm(forms.ModelForm):
  class Meta:
    model = Location
    fields = [ ]


####################
# Other - approach #
####################

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