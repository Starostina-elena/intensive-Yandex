from django.http import HttpResponse
# from django.shortcuts import render


# Create your views here.
def item_list(request):
    return HttpResponse('<html><body>Список элементов</body></html>')


def item_detail(request, item_id):
    return HttpResponse('<html><body>Подробно элемент</body></html>')
