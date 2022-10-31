from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateGeoInfoLandParcelsContainerForm
from apps.locations.forms import LocationGeoInfoLandParcelsFormSet
from crispy_forms.helper import FormHelper

class LocationDetailGeoInfoLandParcelsView(DetailView):
  model = Location
  template_name = 'locations/panels/geo-info--land-parcels.html'

# Helper for managing the sublist of land parcels.
class LocationGeoInfoLandParcelsFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # land parcels are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-geo-info--land-parcels'

class LocationUpdateGeoInfoLandParcelsView(BaseFormsetUpdateView):
  model = Location
  form_class = LocationUpdateGeoInfoLandParcelsContainerForm
  template_name = 'locations/forms/geo-info--land-parcels.html'
  section_name = 'geo-info--land-parcels'
  table_name = 'land_parcel'
  primary_key = 'land_parcel_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
    context = super(LocationUpdateGeoInfoLandParcelsView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['formset_list'] = LocationGeoInfoLandParcelsFormSet(self.request.POST, instance=self.object)
    else:
        context['formset_list'] = LocationGeoInfoLandParcelsFormSet(instance=self.object)
    context['formset_helper'] = LocationGeoInfoLandParcelsFormHelper()
    return context