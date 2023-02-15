from django.urls import path, re_path, register_converter

from . import converter, views


register_converter(converter.PositiveNumber, 'pos_int')


urlpatterns = [
    path('', views.item_list),
    path('<int:item_id>', views.item_detail),
    path('<pos_int:item_id>', views.item_detail),
    re_path(r're/(?P<item_id>[0-9]+)', views.item_detail)
]
