from django.contrib import admin
from menus.models import MenuItem


class MenuItemInline(admin. StackedInline):
    model = MenuItem
    prepopulated_fields = {'slug': ('name',)}


class MenuItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    inlines = [MenuItemInline]

admin.site.register(MenuItem, MenuItemAdmin)
