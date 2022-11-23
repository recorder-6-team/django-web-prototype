from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.places.models import LocationFeature
from apps.places.forms import LocationFeatureUpdateManagementAimsContainerForm
from apps.places.forms import LocationFeatureManagementAimsFormSet
from crispy_forms.helper import FormHelper

class LocationFeatureDetailManagementAimsView(DetailView):
  model = LocationFeature
  template_name = 'location_features/panels/management-aims.html'

# Helper for managing the sublist of management_aims.
class LocationFeatureManagementAimsFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-feature--management-aims'

class LocationFeatureUpdateManagementAimsView(BaseFormsetUpdateView):
  model = LocationFeature
  form_class = LocationFeatureUpdateManagementAimsContainerForm
  template_name = 'location_features/forms/management-aims.html'
  section_name = 'management-aims'
  table_name = 'management_aim'
  primary_key = 'management_aim_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
    context = super(LocationFeatureUpdateManagementAimsView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['formset_list'] = LocationFeatureManagementAimsFormSet(self.request.POST, instance=self.object)
    else:
        context['formset_list'] = LocationFeatureManagementAimsFormSet(instance=self.object)
    context['formset_helper'] = LocationFeatureManagementAimsFormHelper()
    return context