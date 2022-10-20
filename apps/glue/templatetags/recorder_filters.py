from django import template
from django.template.defaultfilters import stringfilter
from striprtf.striprtf import rtf_to_text

register = template.Library()

# A filter to retrieve the location preferred name.
@register.filter(is_safe=True)
def preferred_name(value):
  for name in value.names.all():
    if name.preferred:
      return name.item_name
  return 'Unknown'

# A filter to retrieve a list of alternative location names.
@register.filter(is_safe=True)
def alternative_names(value):
  return value.names.filter(preferred=0)

# A filter to strip RTF from text in a Recorder 6 database field.
# TODO check if striprtf is still necessary, as handled within models?
# TODO could we convert RTF to HTML?
@register.filter(is_safe=True)
@stringfilter
def striprtf(value):
  return rtf_to_text(value).strip()

# A filter to convert new lines in text into HTML <br> elements.
@register.filter(is_safe=True)
@stringfilter
def newlinetohtml(value):
  return value.replace('\n', '<br/>')