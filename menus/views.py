from django.shortcuts import render
from django.views.generic import View


class MenuItemView(View):

    def get(self, request):
        return render(request, 'menus/menus.html')
