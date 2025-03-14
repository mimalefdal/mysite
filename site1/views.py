from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def index_view(request):
    return render(request,'index.html')

def contact_view(request):
    return render(request,'contact.html')

def about_view(request):
    return render(request,'about.html')

def index_json(request):
    return JsonResponse({
        'status':'OK',
        'location':'home'
        })
