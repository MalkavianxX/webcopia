from email.mime import nonmultipart
from django.db import models


class Ventas_por_enviar(models.Model):

    enviado = models.BooleanField(default = False) 
    sesion = models.CharField(max_length=1000)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    telefono = models.CharField(max_length= 50)
    email = models.CharField(max_length=200)
    municipio = models.CharField(max_length=200)
    colonia = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=200)
    calle = models.CharField(max_length=200)
    num_exterior = models.CharField(max_length=200)
    num_interior = models.CharField(max_length=200)
    referencias = models.CharField(max_length=1000)
    envio = models.CharField(max_length=200) 
    total = models.CharField(max_length=200)
    productos = models.CharField(max_length=1000)
    cantidad = models.CharField(max_length=500)
    autorizacion = models.CharField(max_length=10000)
    verificacion = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"  
  