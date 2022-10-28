from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.db import connection
from django.conf import settings
from django.urls import reverse
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateGeoInfoAdminAreasForm
from apps.locations.forms import LocationGeoInfoAdminAreaFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailGeoInfoAdminAreasView(DetailView):
  model = Location
  template_name = 'locations/panels/geo-info--admin-areas.html'

# Helper for managing the sublist of location uses.
class LocationGeoInfoAdminAreasFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # Admin areas are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-geo-info--admin-areas'

class LocationUpdateGeoInfoAdminAreasView(UpdateView):
  model = Location
  form_class = LocationUpdateGeoInfoAdminAreasForm
  template_name = 'locations/forms/geo-info--admin-areas.html'

  # See https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
  # see https://stackoverflow.com/questions/53379841/django-crispy-forms-inline-formsets-managementform-data-error-with-update-vi

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateGeoInfoAdminAreasView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['location__geo_info__admin_areas'] = LocationGeoInfoAdminAreaFormSet(self.request.POST, instance=self.object)
    else:
        context['location__geo_info__admin_areas'] = LocationGeoInfoAdminAreaFormSet(instance=self.object)
    context['admin_areas_helper'] = LocationGeoInfoAdminAreasFormHelper()
    return context

  def form_valid(self, form):
    locationGeoInfoAdminAreasForms = LocationGeoInfoAdminAreaFormSet(self.request.POST, instance=self.object)
    if locationGeoInfoAdminAreasForms.is_valid():
      for locationGeoInfoAdminAreaForm in locationGeoInfoAdminAreasForms:
        if locationGeoInfoAdminAreaForm.cleaned_data.get('DELETE'):
          locationGeoInfoAdminAreaForm.instance.delete()
        else:
          locationGeoInfoAdminArea = locationGeoInfoAdminAreaForm.save(commit=False)
          # Skip rows that aren't filled in.
          if hasattr(locationGeoInfoAdminArea, 'admin_area_key'):
            if locationGeoInfoAdminArea.location_admin_areas_key == '':
              # Raw SQL call to populate the location admin area key.
              with connection.cursor() as cursor:
                cursor.execute("SET nocount on; DECLARE @key CHAR(16); EXEC spNextKey 'location_admin_areas', @key OUTPUT; SELECT @key;")
                row = cursor.fetchone()
                locationGeoInfoAdminArea.location_admin_areas_key = row[0]
              locationGeoInfoAdminArea.entered_by = self.request.user.name_key_id
              locationGeoInfoAdminArea.entry_date = datetime.now()
              locationGeoInfoAdminArea.custodian = settings.SITE_ID
              locationGeoInfoAdminArea.system_supplied_data = False
            else:
              locationGeoInfoAdminArea.changed_by = self.request.user.name_key_id
              locationGeoInfoAdminArea.changed_date = datetime.now()
            # TODO handle case where name save fails
            locationGeoInfoAdminArea.save()
    result = super(UpdateView, self).form_valid(form)
    return result

  # Change the URL on successful post to just return the general section, not
  # the whole location.
  def get_success_url(self):
    return reverse("locations:view-geo-info--admin-areas", kwargs={"pk": self.object.location_key})