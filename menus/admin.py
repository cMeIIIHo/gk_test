from django.contrib import admin
from menus.models import MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

admin.site.register(MenuItem, MenuItemAdmin)
