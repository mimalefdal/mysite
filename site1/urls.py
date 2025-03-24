from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from site1.views import *

urlpatterns = [
    path('', index_view),
    path('contact/', contact_view),
    path('about/', about_view),
    path('api/root/', index_json),
   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)