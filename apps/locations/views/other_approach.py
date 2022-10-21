from django.views.generic.detail import DetailView
from .base_update_view import BaseUpdateView
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateOtherApproachForm

class LocationDetailOtherApproachView(DetailView):
  model = Location
  template_name = 'locations/panels/other-approach.html'

class LocationUpdateOtherApproachView(BaseUpdateView):
  model = Location
  form_class = LocationUpdateOtherApproachForm
  template_name = 'locations/forms/other-approach.html'
  section_name = 'other-approach'