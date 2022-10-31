from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateNamesContainerForm
from apps.locations.forms import LocationNamesFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailNamesView(DetailView):
  model = Location
  template_name = 'locations/panels/names.html'

# Helper for managing the sublist of location names.
class LocationNamesFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # Names are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-names'

class LocationUpdateNamesView(BaseFormsetUpdateView):
  model = Location
  form_class = LocationUpdateNamesContainerForm
  template_name = 'locations/forms/names.html'
  section_name = 'names'
  table_name = 'location_name'
  primary_key = 'location_name_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
    context = super(LocationUpdateNamesView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['formset_list'] = LocationNamesFormSet(self.request.POST, instance=self.object)
    else:
        context['formset_list'] = LocationNamesFormSet(instance=self.object)
    context['formset_helper'] = LocationNamesFormHelper()
    return context