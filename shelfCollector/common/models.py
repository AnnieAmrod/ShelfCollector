from django.db import models


# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(
                            max_length=30,
                            verbose_name='Nombre',
                            unique=True,
                            null=False,
                            blank=False)
    descripcion = models.TextField(
                            verbose_name='Descripcion',
                            max_length=300,
                            null=True,
                            blank=True)

    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def __str__(self):
        return self.nombre


class Carpeta(models.Model):
    nombre = models.CharField(
                            max_length=30,
                            verbose_name='Nombre',
                            unique=True,
                            null=False,
                            blank=False)
    descripcion = models.TextField(
                            verbose_name='Descripcion',
                            max_length=300,
                            null=True,
                            blank=True)

    class Meta:
        verbose_name_plural = 'Carpetas'

    def __str__(self):
        return self.nombre
