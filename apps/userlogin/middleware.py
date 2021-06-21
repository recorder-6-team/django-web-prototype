from django.http import HttpResponseRedirect
from django.urls import reverse
from . import apps

def auth_middleware(get_response):
  """Middleware to intercept requests and redirect if not authorised."""

  def middleware(request):
    if not request.user.is_authenticated and request.path != reverse('login'):
      return HttpResponseRedirect(reverse('login')) # or http response
    response = get_response(request)
    return response

  return middleware