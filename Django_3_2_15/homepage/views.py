from django.http import HttpResponse
# from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('<html><body>Главная</body></html>')


def coffee(request):
    return HttpResponse(content='<body>Я чайник</body>', status=418)
