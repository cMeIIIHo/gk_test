from django import template
from django.shortcuts import get_object_or_404
from menus.models import MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.inclusion_tag('menus/menu_tree.html', takes_context=True)
def draw_menu(context, menu_name):
    menu_item = get_object_or_404(MenuItem, name=menu_name)
    return {'menu_item': menu_item}
