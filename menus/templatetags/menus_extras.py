from django import template
from django.shortcuts import get_object_or_404
from menus.models import MenuItem
from django.http import Http404
register = template.Library()


@register.inclusion_tag('menus/menu_tree.html', takes_context=True)
def draw_menu(context, name_or_id):
    if isinstance(name_or_id, str):
        menu_item = get_object_or_404(MenuItem, name=name_or_id)
    elif isinstance(name_or_id, int):
        menu_item = get_object_or_404(MenuItem, pk=name_or_id)
    else:
        raise Http404("No MenuItem matches the given query.")
    return {'menu_item': menu_item}
