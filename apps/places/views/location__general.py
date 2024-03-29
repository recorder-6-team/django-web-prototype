from django.views.generic.detail import DetailView
from .base_update_view import BaseUpdateView
from apps.places.models import Location
from apps.places.forms import LocationUpdateGeneralForm

class LocationDetailGeneralView(DetailView):
  model = Location
  template_name = 'locations/panels/general.html'

# View for the location general section update form.
class LocationUpdateGeneralView(BaseUpdateView):
  model = Location
  form_class = LocationUpdateGeneralForm
  template_name = 'locations/forms/general.html'
  section_name = 'general'