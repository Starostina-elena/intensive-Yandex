from catalog import models

from django.shortcuts import get_object_or_404, render


def item_list(request):
    template = 'catalog/item_list.html'
    items = models.Item.objects.published().order_by(
        models.Item.category.field.name,
        models.Item.name.field.name,
        models.Item.id.field.name)
    context = {'items_list': items}
    return render(request, template, context)


def item_detail(request, item_id):
    template = 'catalog/item_detail.html'
    item = get_object_or_404(
        models.Item.objects.published(),
        id=item_id
    )
    gallery = list(models.PhotoForGallery.objects.filter(item=item_id))
    context = {'item': item,
               'album': gallery if gallery else None}
    return render(request, template, context)
