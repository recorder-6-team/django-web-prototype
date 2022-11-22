from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.places.models import Location
from apps.places.forms import LocationUpdateOtherTenuresContainerForm
from apps.places.forms import LocationOtherTenuresFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailOtherTenuresView(DetailView):
  model = Location
  template_name = 'locations/panels/other--tenures.html'

# Helper for managing the sublist of location tenures.
class LocationOtherTenuresFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # Admin areas are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location--other--tenures'

class LocationUpdateOtherTenuresView(BaseFormsetUpdateView):
  model = Location
  form_class = LocationUpdateOtherTenuresContainerForm
  template_name = 'locations/forms/other--tenures.html'
  section_name = 'other--tenures'
  table_name = 'tenure'
  primary_key = 'tenure_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
      context = super(LocationUpdateOtherTenuresView, self).get_context_data(**kwargs)
      if self.request.POST:
          context['formset_list'] = LocationOtherTenuresFormSet(self.request.POST, instance=self.object)
      else:
          context['formset_list'] = LocationOtherTenuresFormSet(instance=self.object)
      context['formset_helper'] = LocationOtherTenuresFormHelper()
      return context