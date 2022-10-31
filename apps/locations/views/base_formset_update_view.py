from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.db import connection
from django.conf import settings
from django.urls import reverse
from datetime import datetime

class BaseFormsetUpdateView(UpdateView):
  section_name = ''
  table_name = ''
  primary_key = ''

  # POST form data handler.
  #
  # Checks for the cancel button and redirects to bypass the form save.
  def post(self, request, *args, **kwargs):
    self.object = self.get_object()
    if 'cancel' in request.POST:
      url = self.get_success_url()
      return HttpResponseRedirect(url)
    else:
      return super().post(request, args, kwargs)

  # Custom form_valid method.
  #
  # * Checks the deletion checkbox and deletes records.
  # * Determines if a row contains data. Skips if not.
  # * Determines if doing an insert or update and sets correct table metadata.
  # * If doing insert, generates a new NBN key value.
  def form_valid(self, form):
    context = self.get_context_data()
    formset_list = context['formset_list']
    print(form.cleaned_data)
    if formset_list.is_valid():
      for this_form in formset_list:
        # Check if delete checkbox ticked.
        if this_form.cleaned_data.get('DELETE'):
          this_form.instance.delete()
        else:
          # Skip rows that aren't filled in or haven't been changed.
          if this_form.has_changed():
            validated_form = this_form.save(commit=False)
            # If the PK is empty, create a new key so do an insert.
            if getattr(validated_form, self.primary_key) == '':
              # Raw SQL call to populate the location land parcel key.
              with connection.cursor() as cursor:
                cursor.execute("SET nocount on; DECLARE @key CHAR(16); EXEC spNextKey '" + self.table_name + "', @key OUTPUT; SELECT @key;")
                row = cursor.fetchone()
                setattr(validated_form, self.primary_key, row[0])
              # Doing insert, so set entry metadata.
              validated_form.entered_by = self.request.user.name_key_id
              validated_form.entry_date = datetime.now()
              validated_form.custodian = settings.SITE_ID
              validated_form.system_supplied_data = False
            else:
              # Doing update, so set changed metadata.
              validated_form.changed_by = self.request.user.name_key_id
              validated_form.changed_date = datetime.now()
            # TODO handle case where name save fails
            validated_form.save()
      return super(UpdateView, self).form_valid(form)
    else:
      return self.render_to_response(self.get_context_data(form=form))

  # Change the URL on successful post to just return the general section, not
  # the whole location.
  def get_success_url(self):
    return reverse("locations:view-" + self.section_name, kwargs={"pk": self.object.location_key})