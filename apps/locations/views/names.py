from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.db import connection
from django.conf import settings
from django.urls import reverse
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateNamesForm
from apps.locations.forms import LocationNameFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailNamesView(DetailView):
  model = Location
  template_name = 'locations/includes/view/names.html'

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

class LocationUpdateNamesView(UpdateView):
  model = Location
  form_class = LocationUpdateNamesForm
  template_name = 'locations/forms/names.html'

  # See https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
  # see https://stackoverflow.com/questions/53379841/django-crispy-forms-inline-formsets-managementform-data-error-with-update-vi

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateNamesView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['locationnames'] = LocationNameFormSet(self.request.POST, instance=self.object)
    else:
        context['locationnames'] = LocationNameFormSet(instance=self.object)
    context['names_helper'] = LocationNamesFormHelper()
    return context

  def form_valid(self, form):
    locationNamesForms = LocationNameFormSet(self.request.POST, instance=self.object)
    if locationNamesForms.is_valid():
      for locationNameForm in locationNamesForms:
        if locationNameForm.cleaned_data.get('DELETE'):
          locationNameForm.instance.delete()
        else:
          locationName = locationNameForm.save(commit=False)
          # Skip rows that aren't filled in.
          if locationName.item_name.strip() != '':
            # Null preferreds must be set to false
            # TODO - is there a better way to do this?
            if locationName.preferred == None:
              locationName.preferred = False
            if locationName.location_name_key == '':
              # Raw SQL call to populate the location name key.
              with connection.cursor() as cursor:
                cursor.execute("SET nocount on; DECLARE @key CHAR(16); EXEC spNextKey 'location_name', @key OUTPUT; SELECT @key;")
                row = cursor.fetchone()
                locationName.location_name_key = row[0]
              locationName.entered_by = self.request.user.name_key_id
              locationName.entry_date = datetime.now()
              locationName.custodian = settings.SITE_ID
            else:
              locationName.changed_by = self.request.user.name_key_id
              locationName.changed_date = datetime.now()
            # TODO handle case where name save fails
            locationName.save()
    result = super(UpdateView, self).form_valid(form)
    return result

  # Change the URL on successful post to just return the general section, not
  # the whole location.
  def get_success_url(self):
    return reverse("locations:view-names", kwargs={"pk": self.object.location_key})