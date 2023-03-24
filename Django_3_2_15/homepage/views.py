from catalog import models

from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):
    template = 'homepage/homepage.html'
    items = models.Item.objects.published().filter(
        is_on_main=True
        ).order_by(models.Item.name.field.name,
                   models.Item.id.field.name)
    context = {'items_list': items}
    return render(request, template, context)


def coffee(request):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.get_username())
        user.profile.coffee_count += 1
        user.profile.save()
    template = 'homepage/coffee.html'
    context = {}
    return render(request, template, context, status=418)
