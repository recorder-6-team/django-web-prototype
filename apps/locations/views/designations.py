from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.db import connection
from django.conf import settings
from django.urls import reverse
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateDesignationsForm
from apps.locations.forms import LocationDesignationFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailDesignationsView(DetailView):
  model = Location
  template_name = 'locations/includes/view/designations.html'

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

class LocationUpdateDesignationsView(UpdateView):
  model = Location
  form_class = LocationUpdateDesignationsForm
  template_name = 'locations/forms/designations.html'

  # See https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
  # see https://stackoverflow.com/questions/53379841/django-crispy-forms-inline-formsets-managementform-data-error-with-update-vi

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateDesignationsView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['locationdesignations'] = LocationDesignationFormSet(self.request.POST, instance=self.object)
    else:
        context['locationdesignations'] = LocationDesignationFormSet(instance=self.object)
    context['designations_helper'] = LocationDesignationsFormHelper()
    return context

  def form_valid(self, form):
    locationDesignationsForms = LocationDesignationFormSet(self.request.POST, instance=self.object)
    if locationDesignationsForms.is_valid():
      for locationDesignationForm in locationDesignationsForms:
        if locationDesignationForm.cleaned_data.get('DELETE'):
          locationDesignationForm.instance.delete()
        else:
          locationDesignation = locationDesignationForm.save(commit=False)
          # Skip rows that aren't filled in.
          if locationDesignation.site_status_key != '':
            if locationDesignation.designation_key == '':
              # Raw SQL call to populate the location designation key.
              with connection.cursor() as cursor:
                cursor.execute("SET nocount on; DECLARE @key CHAR(16); EXEC spNextKey 'location_designation', @key OUTPUT; SELECT @key;")
                row = cursor.fetchone()
                locationDesignation.designation_key = row[0]
              locationDesignation.entered_by = self.request.user.name_key_id
              locationDesignation.entry_date = datetime.now()
              locationDesignation.custodian = settings.SITE_ID
              locationDesignation.system_supplied_data = False
            else:
              locationDesignation.changed_by = self.request.user.name_key_id
              locationDesignation.changed_date = datetime.now()
            # TODO handle case where name save fails
            locationDesignation.save()
    result = super(UpdateView, self).form_valid(form)
    return result

  # Change the URL on successful post to just return the general section, not
  # the whole location.
  def get_success_url(self):
    return reverse("locations:view-designations", kwargs={"pk": self.object.location_key})