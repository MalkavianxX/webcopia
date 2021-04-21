from django.urls import path
from . import views


urlpatterns = [
    path('',views.mayoristas,name="mayoristas"),
     
]

 