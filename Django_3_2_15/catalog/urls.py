from django.urls import path, re_path, register_converter

from . import converter, views


register_converter(converter.PositiveNumber, 'pos_int')

app_name = 'catalog'

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:item_id>', views.item_detail, name='item_detail'),
    path('convertor/<pos_int:item_id>', views.item_detail),
    re_path(r're/(?P<item_id>[1-9][0-9]*)', views.item_detail)
]
