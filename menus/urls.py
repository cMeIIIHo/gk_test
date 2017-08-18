from django.conf.urls import url
from menus.views import MenuItemView
# from menus.views import menu_item

app_name = 'menus'

urlpatterns = [
    url(r'^$', MenuItemView.as_view(), name='menu_item_view'),
    url(r'^test/$', MenuItemView.as_view(), name='test_url'),
]
