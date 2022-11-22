from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.places.models import Location
from apps.places.forms import LocationUpdateOtherRelationsContainerForm
from apps.places.forms import LocationOtherRelationsFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailOtherRelationsView(DetailView):
  model = Location
  template_name = 'locations/panels/other--relations.html'

# Helper for managing the sublist of location relations.
class LocationOtherRelationsFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # Admin areas are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location--other--relations'

class LocationUpdateOtherRelationsView(BaseFormsetUpdateView):
  model = Location
  form_class = LocationUpdateOtherRelationsContainerForm
  template_name = 'locations/forms/other--relations.html'
  section_name = 'other--relations'
  table_name = 'location_relation'
  primary_key = 'location_relation_key'

  # Method to create the formset and helper for the template.
  def get_context_data(self, **kwargs):
      context = super(LocationUpdateOtherRelationsView, self).get_context_data(**kwargs)
      if self.request.POST:
          context['formset_list'] = LocationOtherRelationsFormSet(self.request.POST, instance=self.object)
      else:
          context['formset_list'] = LocationOtherRelationsFormSet(instance=self.object)
      context['formset_helper'] = LocationOtherRelationsFormHelper()
      return context