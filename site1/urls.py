from django.contrib import admin
from django.urls import path
from site1.views import *

urlpatterns = [
    path('', home_view),
    path('api/root/', home_json),
   
]