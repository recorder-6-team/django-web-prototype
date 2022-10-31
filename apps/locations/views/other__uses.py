from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateOtherUsesContainerForm
from apps.locations.forms import LocationOtherUsesFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailOtherUsesView(DetailView):
  model = Location
  template_name = 'locations/panels/other--uses.html'

# Helper for managing the sublist of location uses.
class LocationOtherUsesFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # Admin areas are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-other--uses'

class LocationUpdateOtherUsesView(BaseFormsetUpdateView):
  model = Location
  form_class = LocationUpdateOtherUsesContainerForm
  template_name = 'locations/forms/other--uses.html'
  section_name = 'other--uses'
  table_name = 'location_use'
  primary_key = 'location_use_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
      context = super(LocationUpdateOtherUsesView, self).get_context_data(**kwargs)
      if self.request.POST:
          context['formset_list'] = LocationOtherUsesFormSet(self.request.POST, instance=self.object)
      else:
          context['formset_list'] = LocationOtherUsesFormSet(instance=self.object)
      context['formset_helper'] = LocationOtherUsesFormHelper()
      return context