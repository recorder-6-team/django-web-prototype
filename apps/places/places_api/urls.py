from django.urls import include, path
from rest_framework import routers
from . import views

placesRouter = routers.DefaultRouter()
placesRouter.register(r'location/list', views.LocationViewSet, basename='location')
placesRouter.register(r'location-feature/list', views.LocationFeatureViewSet, basename='location-feature')

app_name = 'places_api'

print(placesRouter.get_urls())

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(placesRouter.urls)),
]