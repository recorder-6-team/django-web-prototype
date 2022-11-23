from django.urls import path

from .views import location
from .views import location__names
from .views import location__general
from .views import location__designations
from .views import location__geo_info__admin_areas
from .views import location__geo_info__land_parcels
from .views import location__other__relations
from .views import location__other__uses
from .views import location__other__tenures
from .views import location__other__approach
from .views import location_feature
from .views import location_feature__general
from .views import location_feature__damage_occurrences

app_name = 'places'
urlpatterns = [
  ## Locations ##
  # Locations main page.
  path('', location.LocationListView.as_view(), name='index'),
  # Full details view, normally loaded into main page via AJAX when a node
  # selected.
  path('location/<str:pk>/', location.LocationDetailView.as_view(), name='view--locations'),
  # Section details views, normally loaded into main page via AJAX after a form post.
  path('location/<str:pk>/view/names', location__names.LocationDetailNamesView.as_view(), name='view--location--names'),
  path('location/<str:pk>/view/general', location__general.LocationDetailGeneralView.as_view(), name='view--location--general'),
  path('location/<str:pk>/view/designations', location__designations.LocationDetailDesignationsView.as_view(), name='view--location--designations'),
  path('location/<str:pk>/view/geo-info--admin-areas', location__geo_info__admin_areas.LocationDetailGeoInfoAdminAreasView.as_view(), name='view--location--geo-info--admin-areas'),
  path('location/<str:pk>/view/geo-info--land-parcels', location__geo_info__land_parcels.LocationDetailGeoInfoLandParcelsView.as_view(), name='view--location--geo-info--land-parcels'),
  path('location/<str:pk>/view/other--relations', location__other__relations.LocationDetailOtherRelationsView.as_view(), name='view--location--other--relations'),
  path('location/<str:pk>/view/other--uses', location__other__uses.LocationDetailOtherUsesView.as_view(), name='view--location--other--uses'),
  path('location/<str:pk>/view/other--tenures', location__other__tenures.LocationDetailOtherTenuresView.as_view(), name='view--location--other--tenures'),
  path('location/<str:pk>/view/other--approach', location__other__approach.LocationDetailOtherApproachView.as_view(), name='view--location--other--approach'),
  # Individual section forms, loaded via AJAX.
  path('location/<str:pk>/update/names', location__names.LocationUpdateNamesView.as_view(), name='update--location--names'),
  path('location/<str:pk>/update/general', location__general.LocationUpdateGeneralView.as_view(), name='update--location--general'),
  path('location/<str:pk>/update/designations', location__designations.LocationUpdateDesignationsView.as_view(), name='update--location--designations'),
  path('location/<str:pk>/update/geo-info--admin-areas', location__geo_info__admin_areas.LocationUpdateGeoInfoAdminAreasView.as_view(), name='update--location--geo-info--admin-areas'),
  path('location/<str:pk>/update/geo-info--land-parcels', location__geo_info__land_parcels.LocationUpdateGeoInfoLandParcelsView.as_view(), name='update--location--geo-info--land-parcels'),
  path('location/<str:pk>/update/other--relations', location__other__relations.LocationUpdateOtherRelationsView.as_view(), name='update--location--other--relations'),
  path('location/<str:pk>/update/other--uses', location__other__uses.LocationUpdateOtherUsesView.as_view(), name='update--location--other--uses'),
  path('location/<str:pk>/update/other--tenures', location__other__tenures.LocationUpdateOtherTenuresView.as_view(), name='update--location--other--tenures'),
  path('location/<str:pk>/update/other--approach', location__other__approach.LocationUpdateOtherApproachView.as_view(), name='update--location--other--approach'),

  ## Location features ##
  # Full details view, normally loaded into main page via AJAX when a node selected.
  path('location-feature/<str:pk>/', location_feature.LocationFeatureDetailView.as_view(), name='view--location-features'),
  # Section details views, normally loaded into main page via AJAX after a form post.
  path('location-feature/<str:pk>/view/general', location_feature__general.LocationFeatureDetailGeneralView.as_view(), name='view--location-feature--general'),
  # Individual section forms, loaded via AJAX.
  path('location-feature/<str:pk>/update/general', location_feature__general.LocationFeatureUpdateGeneralView.as_view(), name='update--location-feature--general'),
]