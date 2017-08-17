from django.shortcuts import render
from django.views.generic import View


class MenuItemView(View):

    def get(self, request, intermediate_parameters, menu_item):
        context = {
            'intermediate_parameters': intermediate_parameters,
            'menu_item': menu_item,
        }
        return render(request, 'menus/menus.html', context)

