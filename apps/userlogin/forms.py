from django.contrib.auth.forms import AuthenticationForm

from django.conf import settings

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    organisation = settings.ORGANISATION_NAME