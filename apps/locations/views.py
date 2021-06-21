from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.db import connection
from django.conf import settings

from datetime import datetime

from .models import Location
from .models import LocationName
from .forms import LocationUpdateForm
from .forms import LocationNameFormSet
from crispy_forms.helper import FormHelper

class LocationListView(TemplateView):
  model = Location
  template_name = 'locations/index.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['externalJs'] = [
      'https://cdnjs.cloudflare.com/ajax/libs/jstree/3.3.8/jstree.min.js',
      'https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/build/ol.js',
    ]
    context['externalCss'] = [
      'https://cdnjs.cloudflare.com/ajax/libs/jstree/3.3.8/themes/default/style.min.css',
      'https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/css/ol.css',
    ]
    context['internalJs'] = [
      'locations/js/initTree.js',
      'js/initMap.js',
    ]
    return context

class LocationDetailView(DetailView):
  model = Location

  # Enable AJAX request for details without HTML template, so it can be shown alongside treeview.
  def get_template_names(self):
    if self.request.is_ajax():
      # Ajax request for details just renders a details block.
      return [
        'locations/ajax/detail.html',
      ]
    else:
      # Non-ajax request for details renders a full-page.
      return [
        'locations/detail.html',
      ]

  # Attach map assets for non-ajax locations detail view.
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if not self.request.is_ajax():
      context['externalJs'] = [
        'https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/build/ol.js',
      ]
      context['externalCss'] = [
        'https://cdn.jsdelivr.net/gh/openlayers/openlayers.github.io@master/en/v6.5.0/css/ol.css',
      ]
      context['internalJs'] = [
        'js/initMap.js',
      ]
      context['recorderData'] = {
        'centreMap': {
          'lat': self.object.lat,
          'lon': self.object.long,
        }
      }
    return context

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

class LocationUpdateView(UpdateView):
  model = Location
  form_class = LocationUpdateForm
  template_name = 'locations/update.html'

  # See https://medium.com/@adandan01/django-inline-formsets-example-mybook-420cc4b6225d
  # see https://stackoverflow.com/questions/53379841/django-crispy-forms-inline-formsets-managementform-data-error-with-update-vi

  def get_context_data(self, **kwargs):
    context = super(LocationUpdateView, self).get_context_data(**kwargs)
    if self.request.POST:
        context['locationnames'] = LocationNameFormSet(self.request.POST, instance=self.object)
    else:
        context['locationnames'] = LocationNameFormSet(instance=self.object)
    context['names_helper'] = LocationNamesFormHelper()
    context['internalJs'] = [
        'locations/js/locationNamesForm.js',
      ]
    return context

  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    locationForm = self.get_form()
    locationNamesForms = LocationNameFormSet(request.POST, instance=self.object)
    # Now validate both the form and any formsets
    if locationForm.is_valid() and locationNamesForms.is_valid():
        # Note - we are passing the names formset to form_valid. If you had more formsets
        # you would pass these as well.
        return self.form_valid(locationForm)
    else:
        for f in locationNamesForms:
          print(f.errors)
        return self.form_invalid(locationForm)

  def form_valid(self, form):
    # TODO metadata and primary key handling needs to go in a mixin or base class.
    if (form.instance.pk):
      form.instance.changed_by = self.request.user.name_key_id
      form.instance.changed_date = datetime.now()
    else:
      form.instance.entered_by = self.request.user.name_key_id
      form.instance.entered_date = datetime.now()


    result = super(LocationUpdateView, self).form_valid(form)
    locationNamesForms = LocationNameFormSet(self.request.POST, instance=self.object)
    if locationNamesForms.is_valid():
      for locationNameForm in locationNamesForms:
        locationName = locationNameForm.save(commit=False)
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

    return result