from django.urls import path, include

from .views import LocationDetailView
from .views import LocationListView
from .views import LocationUpdateGeneralView
from .views import LocationUpdateOtherApproachView

app_name = 'locations'
urlpatterns = [
    # Locations main page.
    path('', LocationListView.as_view(), name='index'),
    # Details view, normally loaded into main page via AJAX.
    path('<str:pk>/', LocationDetailView.as_view(), name='view'),
    # Individual section forms, loaded via AJAX.
    path('<str:pk>/update-general', LocationUpdateGeneralView.as_view(), name='updateGeneral'),
    path('<str:pk>/update-other-approach', LocationUpdateOtherApproachView.as_view(), name='updateOtherApproach'),


]