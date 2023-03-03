from catalog import models

from django.shortcuts import render


def item_list(request):
    template = 'catalog/item_list.html'
    context = {'items_list':
               list(models.Item.objects.filter(is_published=True))}
    return render(request, template, context)


def item_detail(request, item_id):
    template = 'catalog/item_detail.html'
    obj = models.Item.objects.get(id=item_id)
    context = {'item': obj,
               'item_tags': list(obj.tags.filter(is_published=True))}
    return render(request, template, context)
