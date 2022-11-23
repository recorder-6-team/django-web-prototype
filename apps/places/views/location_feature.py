# Views for the entire location, including index page and details view.
from django.views.generic.detail import DetailView
from apps.places.models import LocationFeature

class LocationFeatureDetailView(DetailView):
  model = LocationFeature

  # Is the request AJAX?
  def __request_is_ajax(self):
    return self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

  # Enable AJAX request for details without HTML template, so it can be shown alongside treeview.
  def get_template_names(self):
    if self.__request_is_ajax():
      # Ajax request for details just renders a details block.
      return [
        'location_features/detail.html',
      ]
    else:
      # Non-ajax request for details renders a full-page.
      return [
        'location_features/detail-container.html',
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
        'places/js/initMap.js',
        'places/js/locationFeatureFormEditButtons.js',
      ]
      context['recorderData'] = {
        'centreMap': {
          'lat': self.object.location_key.lat,
          'lon': self.object.location_key.long,
        }
      }
    return context