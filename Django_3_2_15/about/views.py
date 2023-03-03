from django.shortcuts import render


# Create your views here.
def description(request):
    template = 'about/about.html'
    context = {}
    return render(request, template, context)
