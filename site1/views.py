from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def home_view(request):
    return HttpResponse('<h1>Home Page</h1>')

def home_json(request):
    return JsonResponse({
        'status':'OK',
        'location':'home'
        })
