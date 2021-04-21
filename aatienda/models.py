
from django.db import models

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "cateogriaProd"
        verbose_name_plural = "categoriasProd"

    def __str__(self):
        return self.nombre

 
class Prodcuto(models.Model):
    nombre = models.CharField(max_length=100)
    categorias = models.ForeignKey(CategoriaProd, on_delete = models.CASCADE)
    imagen = models.ImageField(upload_to= "aatienda", null = True, blank = True)
    precio = models.FloatField()
    dosponibilidad = models.BooleanField(default = True) 
    descripccion = models.CharField(max_length = 200, null= True, blank= True)
    stock =models.IntegerField()
    codigo_modelo =models.CharField(max_length=50,null=True, blank=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)             
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"    


            