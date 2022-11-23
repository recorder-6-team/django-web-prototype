from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.places.models import LocationFeature
from apps.places.forms import LocationFeatureUpdatePotentialThreatsContainerForm
from apps.places.forms import LocationFeaturePotentialThreatsFormSet
from crispy_forms.helper import FormHelper

class LocationFeatureDetailPotentialThreatsView(DetailView):
  model = LocationFeature
  template_name = 'location_features/panels/potential-threats.html'

# Helper for managing the sublist of potential_threats.
class LocationFeaturePotentialThreatsFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-feature--potential-threats'

class LocationFeatureUpdatePotentialThreatsView(BaseFormsetUpdateView):
  model = LocationFeature
  form_class = LocationFeatureUpdatePotentialThreatsContainerForm
  template_name = 'location_features/forms/potential-threats.html'
  section_name = 'potential-threats'
  table_name = 'potential_threat'
  primary_key = 'potential_threat_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
    context = super(LocationFeatureUpdatePotentialThreatsView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['formset_list'] = LocationFeaturePotentialThreatsFormSet(self.request.POST, instance=self.object)
    else:
        context['formset_list'] = LocationFeaturePotentialThreatsFormSet(instance=self.object)
    context['formset_helper'] = LocationFeaturePotentialThreatsFormHelper()
    return context