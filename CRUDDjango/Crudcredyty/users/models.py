from django.db import models
from ckeditor.fields import RichTextField

class User(models.Model):

    Nombre = models.CharField(verbose_name="Nombre", max_length=50)
    Apellido = models.CharField(verbose_name="Apellido", max_length=50)
    Edad = models.SmallIntegerField(verbose_name="Edad", default=0)
    Profesion = models.CharField(verbose_name="Profesion", max_length=100)
    Perfil = RichTextField(verbose_name="Contenido")
    Creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    Actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")    

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['Creado']

    def __str__(self):
        return self.Nombre
