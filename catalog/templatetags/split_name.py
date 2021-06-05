from django import template

register = template.Library()

@register.filter(name="split_name")
def split_name(value):
    return value.split(" ")