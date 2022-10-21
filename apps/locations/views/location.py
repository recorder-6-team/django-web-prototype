# Views for the entire location, including index page and details view.

from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from apps.locations.models import Location, LocationType

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
      'locations/js/locationFormEditButtons.js',
      'locations/js/locationNamesForm.js',
      'js/initMap.js',
    ]
    context['locationTypes'] = LocationType.objects.all()
    return context

class LocationDetailView(DetailView):
  model = Location

  # Is the request AJAX?
  def __request_is_ajax(self):
    return self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

  # Enable AJAX request for details without HTML template, so it can be shown alongside treeview.
  def get_template_names(self):
    if self.__request_is_ajax():
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
    if not self.__request_is_ajax():
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

