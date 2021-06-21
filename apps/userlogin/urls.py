from django.urls import path, include
from django.contrib.auth import views

from .forms import UserLoginForm

urlpatterns = [
    # Override login.
    path(
        'login/',
        views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=UserLoginForm
        ),
        name='login'
    ),
    # Other auth related URLs remain as default.
    path('', include('django.contrib.auth.urls')),
]