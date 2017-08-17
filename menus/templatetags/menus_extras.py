from django import template
from django.shortcuts import get_object_or_404
from menus.models import MenuItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.inclusion_tag('menus/menu_tree.html', takes_context=True)
def draw_menu(context, menu_name):
    menu = get_object_or_404(MenuItem, name=menu_name, parent=None)
    return {'menu_item': context['menu_item'], 'menu': menu}
