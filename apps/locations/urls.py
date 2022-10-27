from django.urls import path

from .views import location
from .views import names
from .views import general
from .views import designations
from .views import geo_info__admin_areas
from .views import other__approach

app_name = 'locations'
urlpatterns = [
  # Locations main page.
  path('', location.LocationListView.as_view(), name='index'),
  # Full details view, normally loaded into main page via AJAX when a node
  # selected.
  path('<str:pk>/', location.LocationDetailView.as_view(), name='view'),
  # Section details views, normally loaded into main page via AJAX after a form post.
  path('<str:pk>/view/names', names.LocationDetailNamesView.as_view(), name='view-names'),
  path('<str:pk>/view/general', general.LocationDetailGeneralView.as_view(), name='view-general'),
  path('<str:pk>/view/designations', designations.LocationDetailDesignationsView.as_view(), name='view-designations'),
  path('<str:pk>/view/geo-info--admin-areas', geo_info__admin_areas.LocationDetailGeoInfoAdminAreasView.as_view(), name='view-geo-info--admin-areas'),
  path('<str:pk>/view/other--approach', other__approach.LocationDetailOtherApproachView.as_view(), name='view-other--approach'),
  # Individual section forms, loaded via AJAX.
  path('<str:pk>/update/names', names.LocationUpdateNamesView.as_view(), name='update-names'),
  path('<str:pk>/update/general', general.LocationUpdateGeneralView.as_view(), name='update-general'),
  path('<str:pk>/update/designations', designations.LocationUpdateDesignationsView.as_view(), name='update-designations'),
  path('<str:pk>/update/geo-info--admin-areas', geo_info__admin_areas.LocationUpdateGeoInfoAdminAreasView.as_view(), name='update-geo-info--admin-areas'),
  path('<str:pk>/update/other--approach', other__approach.LocationUpdateOtherApproachView.as_view(), name='update-other--approach'),
]