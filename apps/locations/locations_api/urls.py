from django.urls import include, path
from rest_framework import routers
from . import views

locationsRouter = routers.DefaultRouter()
locationsRouter.register(r'list', views.LocationViewSet, basename='location')

app_name = 'locations_api'

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(locationsRouter.urls)),
]