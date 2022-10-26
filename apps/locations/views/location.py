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
      'https://cdn.jsdelivr.net/npm/ol@v7.1.0/dist/ol.js',
      'https://unpkg.com/split.js/dist/split.min.js',
    ]
    context['externalCss'] = [
      'https://cdnjs.cloudflare.com/ajax/libs/jstree/3.3.8/themes/default/style.min.css',
      'https://cdn.jsdelivr.net/npm/ol@v7.1.0/ol.css',
    ]
    context['internalJs'] = [
      'locations/js/initMap.js',
      'locations/js/initTree.js',
      'locations/js/locationFormEditButtons.js',
      'locations/js/locationNamesForm.js',
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
        'locations/detail.html',
      ]
    else:
      # Non-ajax request for details renders a full-page.
      return [
        'locations/detail-container.html',
      ]

  # Attach map and other assets for non-ajax locations detail view.
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    if not self.__request_is_ajax():
      context['externalJs'] = [
        'https://cdn.jsdelivr.net/npm/ol@v7.1.0/dist/ol.js',
        'https://unpkg.com/split.js/dist/split.min.js',
      ]
      context['externalCss'] = [
        'https://cdn.jsdelivr.net/npm/ol@v7.1.0/ol.css',
      ]
      context['internalJs'] = [
        'locations/js/initMap.js',
        'locations/js/locationFormEditButtons.js',
        'locations/js/locationNamesForm.js',
      ]
      context['recorderData'] = {
        'centreMap': {
          'lat': self.object.lat,
          'lon': self.object.long,
        }
      }
    return context

