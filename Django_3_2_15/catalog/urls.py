from django.urls import path, re_path, register_converter

from . import views


class PositiveNumber:
    regex = '([0-9]+)'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)


register_converter(PositiveNumber, 'pos_int')


urlpatterns = [
    path('', views.item_list),
    path('<int:item_id>', views.item_detail),
    path('<pos_int:item_id>', views.item_detail),
    re_path(r'([^/]*)/(?P<item_id>[0-9]+)', views.item_detail)
]
