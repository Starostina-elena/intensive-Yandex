from django.http import HttpResponse
# from django.shortcuts import render


# Create your views here.
def description(request):
    return HttpResponse('<html><body>О проекте</body></html>')
