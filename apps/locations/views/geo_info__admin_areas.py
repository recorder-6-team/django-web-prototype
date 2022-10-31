from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateGeoInfoAdminAreasContainerForm
from apps.locations.forms import LocationGeoInfoAdminAreasFormSet
from crispy_forms.helper import FormHelper

class LocationDetailGeoInfoAdminAreasView(DetailView):
  model = Location
  template_name = 'locations/panels/geo-info--admin-areas.html'

# Helper for managing the sublist of location admin areas.
class LocationGeoInfoAdminAreasFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # Admin areas are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-geo-info--admin-areas'

class LocationUpdateGeoInfoAdminAreasView(BaseFormsetUpdateView):
  model = Location
  form_class = LocationUpdateGeoInfoAdminAreasContainerForm
  template_name = 'locations/forms/geo-info--admin-areas.html'
  section_name = 'geo-info--admin-areas'
  table_name = 'location_admin_areas'
  primary_key = 'location_admin_areas_key'

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateGeoInfoAdminAreasView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['formset_list'] = LocationGeoInfoAdminAreasFormSet(self.request.POST, instance=self.object)
    else:
        context['formset_list'] = LocationGeoInfoAdminAreasFormSet(instance=self.object)
    context['formset_helper'] = LocationGeoInfoAdminAreasFormHelper()
    return context