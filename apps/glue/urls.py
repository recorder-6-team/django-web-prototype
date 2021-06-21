from django.urls import path

from .views import AboutView
from .views import HomeView

app_name = 'glue'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
]