from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.db import connection
from django.conf import settings
from django.urls import reverse
from apps.locations.models import Location
from apps.locations.forms import LocationUpdateGeoInfoLandParcelsForm
from apps.locations.forms import LocationGeoInfoLandParcelFormSet
from crispy_forms.helper import FormHelper
from datetime import datetime

class LocationDetailGeoInfoLandParcelsView(DetailView):
  model = Location
  template_name = 'locations/panels/geo-info--land-parcels.html'

# Helper for managing the sublist of land parcels.
class LocationGeoInfoLandParcelsFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = 'post'
        self.render_required_fields = True
        # land parcels are nested in the location form, so don't need <form> element.
        self.form_tag = False
        self.template = 'bootstrap5/table_inline_formset.html'
        self.form_id='location-geo-info--land-parcels'

class LocationUpdateGeoInfoLandParcelsView(UpdateView):
  model = Location
  form_class = LocationUpdateGeoInfoLandParcelsForm
  template_name = 'locations/forms/geo-info--land-parcels.html'

  # See https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
  # see https://stackoverflow.com/questions/53379841/django-crispy-forms-inline-formsets-managementform-data-error-with-update-vi

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateGeoInfoLandParcelsView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['location__geo_info__land_parcels'] = LocationGeoInfoLandParcelFormSet(self.request.POST, instance=self.object)
    else:
        context['location__geo_info__land_parcels'] = LocationGeoInfoLandParcelFormSet(instance=self.object)
    context['land_parcels_helper'] = LocationGeoInfoLandParcelsFormHelper()
    return context

  def form_valid(self, form):
    locationGeoInfoLandParcelsForms = LocationGeoInfoLandParcelFormSet(self.request.POST, instance=self.object)
    print ('checking valid')
    if locationGeoInfoLandParcelsForms.is_valid():
      print ('checking valid')
      for locationGeoInfoLandParcelForm in locationGeoInfoLandParcelsForms:
        print ('got a form')
        print(locationGeoInfoLandParcelForm.cleaned_data);
        if locationGeoInfoLandParcelForm.cleaned_data.get('DELETE'):
          locationGeoInfoLandParcelForm.instance.delete()
          print('deleted')
        else:
          locationGeoInfoLandParcel = locationGeoInfoLandParcelForm.save(commit=False)
          # Skip rows that aren't filled in.
          if locationGeoInfoLandParcel.land_parcel_number:
            if locationGeoInfoLandParcel.land_parcel_key == '':
              # Raw SQL call to populate the location land parcel key.
              with connection.cursor() as cursor:
                cursor.execute("SET nocount on; DECLARE @key CHAR(16); EXEC spNextKey 'land_parcel', @key OUTPUT; SELECT @key;")
                row = cursor.fetchone()
                locationGeoInfoLandParcel.land_parcel_key = row[0]
              locationGeoInfoLandParcel.entered_by = self.request.user.name_key_id
              locationGeoInfoLandParcel.entry_date = datetime.now()
              locationGeoInfoLandParcel.custodian = settings.SITE_ID
              locationGeoInfoLandParcel.system_supplied_data = False
            else:
              locationGeoInfoLandParcel.changed_by = self.request.user.name_key_id
              locationGeoInfoLandParcel.changed_date = datetime.now()
            # TODO handle case where name save fails
            locationGeoInfoLandParcel.save()
      return super(UpdateView, self).form_valid(form)
    else:
      print('invalid so render to response')
      return self.render_to_response(self.get_context_data(form=form))

  # Change the URL on successful post to just return the general section, not
  # the whole location.
  def get_success_url(self):
    return reverse("locations:view-geo-info--land-parcels", kwargs={"pk": self.object.location_key})