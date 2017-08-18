from django import template
from django.shortcuts import get_object_or_404
from menus.models import MenuItem
from django.http import Http404
register = template.Library()


@register.inclusion_tag('menus/menu_tree.html')
def draw_menu(menu_name):
    menu = get_object_or_404(MenuItem, name=menu_name)
    return {'menu_item': menu}


@register.inclusion_tag('menus/menu_tree.html')
def draw_menu_item_children(menu_item_id):
    menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
    return {'menu_item': menu_item}
