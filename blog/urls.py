from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('single/<int:id>/', blog_single_view, name='single'),
   
]

