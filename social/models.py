from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)
    name = models.CharField(verbose_name='Red social', max_length=100)
    url = models.CharField(verbose_name='URL', max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Edición')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['name']
    
    def __str__(self):
        return self.name