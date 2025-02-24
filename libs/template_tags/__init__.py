from django import template

from .dictionaries import get_item

register = template.Library()

# register the filters
register.filter(name="get_item", filter_func=get_item)
