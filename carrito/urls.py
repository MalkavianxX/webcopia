from django.urls import path
from . import views

app_name="carrito"

urlpatterns = [
    path('agregar_producto/<int:producto_id>/',views.agregar_producto,name="agregar_producto"),
    path('eliminar_producto/<int:producto_id>/',views.eliminar_producto,name="remover_producto"),
    path('decrementar_producto/<int:producto_id>/',views.decrementar_producto,name="decrementar_producto"),
    path('limpiar/',views.limpiar,name="limpiar"),
]

  