from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

class BaseUpdateView(UpdateView):
  section_name = ''

  # Override form_valid to set the metadata.
  def form_valid(self, form):
    # TODO metadata and primary key handling needs to go in a mixin or base class.
    if (form.instance.pk):
      form.instance.changed_by = self.request.user.name_key_id
      form.instance.changed_date = datetime.now()
    else:
      form.instance.entered_by = self.request.user.name_key_id
      form.instance.entered_date = datetime.now()
    result = super(BaseUpdateView, self).form_valid(form)
    return result

  # POST form data handler.
  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    if 'cancel' in request.POST:
      url = self.get_success_url()
      return HttpResponseRedirect(url)
    else:
      thisForm = self.get_form()
      if thisForm.is_valid():
        return self.form_valid(thisForm)
      else:
        return self.form_invalid(thisForm)

  # Change the URL on successful post to just return the general section, not
  # the whole location.
  def get_success_url(self):
    return reverse("locations:view-" + self.section_name, kwargs={"pk": self.object.location_key})