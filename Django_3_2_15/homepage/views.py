from catalog import models

from django.shortcuts import render


def home(request):
    template = 'homepage/homepage.html'
    items = models.Item.objects.published().filter(
        is_on_main=True
        ).order_by('name', 'id')
    context = {'items_list': items}
    return render(request, template, context)


def coffee(request):
    template = 'homepage/coffee.html'
    context = {}
    return render(request, template, context, status=418)
