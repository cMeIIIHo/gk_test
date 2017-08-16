from django.conf.urls import url
from menus.views import MenuItemView
# from menus.views import menu_item

app_name = 'menus'

urlpatterns = [
    url(r'^(?P<intermediate_parameters>.*)/(?P<menu_item>\w+)/$', MenuItemView.as_view(), name='menu_item_view'),
]

# urlpatterns = [
#     url(r'^(\w+/)+$', menu_item, name='menu_item_view'),
# ]

