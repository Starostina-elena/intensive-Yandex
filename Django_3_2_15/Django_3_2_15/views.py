from django.http import HttpResponse
# from django.shortcuts import render


# Create your views here.
def coffee(request):
    return HttpResponse(content='<body>Я чайник</body>', status=418)
