from django.urls import path, include

from .views import LocationDetailView
from .views import LocationListView
from .views import LocationUpdateView

app_name = 'locations'
urlpatterns = [
    path('', LocationListView.as_view(), name='index'),
    path('<str:pk>/update', LocationUpdateView.as_view(), name='update'),
    path('<str:pk>/', LocationDetailView.as_view(), name='view'),
]