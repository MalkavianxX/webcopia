from django.urls import path
from . import views

urlpatterns = [

    path('',views.tienda,name="tienda"),
    path('collares',views.collares,name="collares"),
    path('tienda',views.aretes, name="aretes"),
    path('anillos',views.anillos,name="anillos"),
    path('juegos',views.juegos,name="juegos"),
    path('mayoreo',views.vmayoreo, name="vmayoreo"),
    path('gargantillas',views.gargantillas,name="gargantillas"),
    path("pulseras",views.pulseras,name="pulseras"),
    path('dijes',views.dijes,name="dijes"),
    path('chokers',views.chokers,name="chokers"),
    path('otros',views.otros,name="otros"),
    path('cuidado',views.cuidado,name="cuidado"),
    path('vista/<int:producto_id>',views.vista,name="vista"), 
    path('mascotas',views.mascotas,name="mascotas"),
] 

 