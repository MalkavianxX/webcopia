from django.urls import path
from tienda import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.incio,name="inicio"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)