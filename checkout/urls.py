from django.urls import path
from . import views


app_name="check" 

urlpatterns = [
    path('',views.checkout,name="checkout"),
    path('resumen',views.resumen,name="resumen"),
    path('pago',views.pago,name="pago"),
    path('cancelado',views.pago_cancelado,name="cancelado"),
    path('exitoso',views.pago_exitoso,name="exitoso"),
    path('hecho',views.hecho,name="hecho"),
]

 