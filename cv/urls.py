from django.urls import path
from cv.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cv'

urlpatterns = [
    path('', index_view, name='index'),
   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
