from django.shortcuts import render


def home(request):
    template = 'homepage/homepage.html'
    context = {}
    return render(request, template, context)


def coffee(request):
    template = 'homepage/coffee.html'
    context = {}
    return render(request, template, context)
