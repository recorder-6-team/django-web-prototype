from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.places.models import LocationFeature
from apps.places.forms import LocationFeatureUpdateDamageOccurrencesContainerForm
from apps.places.forms import LocationFeatureDamageOccurrencesFormSet
from crispy_forms.helper import FormHelper

class LocationFeatureDetailDamageOccurrencesView(DetailView):
  model = LocationFeature
  template_name = 'location_features/panels/damage-occurrences.html'

# Helper for managing the sublist of damage_occurrences.
class LocationFeatureDamageOccurrencesFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-feature--damage-occurrences'

class LocationFeatureUpdateDamageOccurrencesView(BaseFormsetUpdateView):
  model = LocationFeature
  form_class = LocationFeatureUpdateDamageOccurrencesContainerForm
  template_name = 'location_features/forms/damage-occurrences.html'
  section_name = 'damage-occurrences'
  table_name = 'damage_occurrence'
  primary_key = 'damage_occurrence_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
    context = super(LocationFeatureUpdateDamageOccurrencesView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['formset_list'] = LocationFeatureDamageOccurrencesFormSet(self.request.POST, instance=self.object)
    else:
        context['formset_list'] = LocationFeatureDamageOccurrencesFormSet(instance=self.object)
    context['formset_helper'] = LocationFeatureDamageOccurrencesFormHelper()
    return context