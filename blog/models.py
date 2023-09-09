from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Edición')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-created']
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Publicación', default=now)
    image = models.ImageField(verbose_name='Imágen', upload_to='blog', null=True, blank=True)
    # el autor es el User actual, y si se elimina el usuario (on_delete), se eliminan todos sus Posts
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # Alternativa a CASCADE: PROTECT (pero habría que agregar null y blank)
    categories = models.ManyToManyField(Category, verbose_name='Categoría(s)')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    update = models.DateTimeField(auto_now=True, verbose_name='Edición')

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created']
    
    def __str__(self):
        return self.title