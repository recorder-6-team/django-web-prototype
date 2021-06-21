from django import template
from django.template.defaultfilters import stringfilter
from striprtf.striprtf import rtf_to_text

register = template.Library()

@register.filter(is_safe=True)
def preferred_name(value):
  for name in value.names.all():
    if name.preferred:
      return name.item_name
  return 'Unknown'

# TODO check if striprtf is still necessary, as handled within models?

@register.filter(is_safe=True)
@stringfilter
def striprtf(value):
  return rtf_to_text(value).strip()

@register.filter(is_safe=True)
@stringfilter
def newlinetohtml(value):
  return value.replace('\n', '<br/>')