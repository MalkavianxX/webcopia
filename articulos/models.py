from django.db import models

class Articulo(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to = 'articulos')
    creted = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'
    def __str__(self) :
        return self.titulo   
