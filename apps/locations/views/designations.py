from django.views.generic.detail import DetailView
from .base_formset_update_view import BaseFormsetUpdateView
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateDesignationsContainerForm
from apps.locations.forms import LocationDesignationsFormSet
from crispy_forms.helper import FormHelper

class LocationDetailDesignationsView(DetailView):
  model = Location
  template_name = 'locations/panels/designations.html'

# Helper for managing the sublist of location designations.
class LocationDesignationsFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # Designations are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-designations'

class LocationUpdateDesignationsView(BaseFormsetUpdateView):
  model = Location
  form_class = LocationUpdateDesignationsContainerForm
  template_name = 'locations/forms/designations.html'
  section_name = 'designations'
  table_name = 'location_designation'
  primary_key = 'designation_key'

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateDesignationsView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['formset_list'] = LocationDesignationsFormSet(self.request.POST, instance=self.object)
    else:
        context['formset_list'] = LocationDesignationsFormSet(instance=self.object)
    context['formset_helper'] = LocationDesignationsFormHelper()
    return context