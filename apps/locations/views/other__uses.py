from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.db import connection
from django.conf import settings
from django.urls import reverse
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateOtherUseForm
from apps.locations.forms import LocationOtherUseFormSet
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

class LocationUpdateOtherUsesView(UpdateView):
  model = Location
  form_class = LocationUpdateOtherUseForm
  template_name = 'locations/forms/other--uses.html'

  # See https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
  # see https://stackoverflow.com/questions/53379841/django-crispy-forms-inline-formsets-managementform-data-error-with-update-vi

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateOtherUsesView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['location__other__uses'] = LocationOtherUseFormSet(self.request.POST, instance=self.object)
    else:
        context['location__other__uses'] = LocationOtherUseFormSet(instance=self.object)
    context['admin_areas_helper'] = LocationOtherUsesFormHelper()
    return context

  def form_valid(self, form):
    locationOtherUsesForms = LocationOtherUseFormSet(self.request.POST, instance=self.object)
    if locationOtherUsesForms.is_valid():
      for locationOtherUseForm in locationOtherUsesForms:
        if locationOtherUseForm.cleaned_data.get('DELETE'):
          locationOtherUseForm.instance.delete()
        else:
          locationOtherUse = locationOtherUseForm.save(commit=False)
          # Skip rows that aren't filled in.
          if locationOtherUse.location_use:
            if locationOtherUse.location_use_key == '':
              # Raw SQL call to populate the location admin area key.
              with connection.cursor() as cursor:
                cursor.execute("SET nocount on; DECLARE @key CHAR(16); EXEC spNextKey 'location_use', @key OUTPUT; SELECT @key;")
                row = cursor.fetchone()
                locationOtherUse.location_use_key = row[0]
              locationOtherUse.entered_by = self.request.user.name_key_id
              locationOtherUse.entry_date = datetime.now()
              locationOtherUse.custodian = settings.SITE_ID
              locationOtherUse.system_supplied_data = False
            else:
              locationOtherUse.changed_by = self.request.user.name_key_id
              locationOtherUse.changed_date = datetime.now()
            # TODO handle case where name save fails
            locationOtherUse.save()
    result = super(UpdateView, self).form_valid(form)
    return result

  # Change the URL on successful post to just return the general section, not
  # the whole location.
  def get_success_url(self):
    return reverse("locations:view-other--uses", kwargs={"pk": self.object.location_key})