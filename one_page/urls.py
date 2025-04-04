from django.urls import path
from one_page.views import *

app_name = 'onepage'

urlpatterns = [
    path('', landing_view, name='index'),
   
]

