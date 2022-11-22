from django.views.generic.detail import DetailView
from .base_update_view import BaseUpdateView
from apps.places.models import LocationFeature
from apps.places.forms import LocationFeatureUpdateGeneralForm

class LocationFeatureDetailGeneralView(DetailView):
  model = LocationFeature
  template_name = 'location_features/panels/general.html'

# View for the location general section update form.
class LocationFeatureUpdateGeneralView(BaseUpdateView):
  model = LocationFeature
  form_class = LocationFeatureUpdateGeneralForm
  template_name = 'location_features/forms/general.html'
  section_name = 'general'