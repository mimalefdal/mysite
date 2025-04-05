from django.urls import path
from one_page.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'onepage'

urlpatterns = [
    path('', landing_view, name='index'),
   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
