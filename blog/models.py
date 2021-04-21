from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    creted = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categoria'
    def __str__(self) :
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to = 'blog',null=True, blank=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    creted = models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    def __str__(self) :
        return self.titulo                