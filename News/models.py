from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="news", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url = models.URLField(blank=True)    

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])