from django.db import models

# Create your models here.
from common.models import Genero, Carpeta


class Autor(models.Model):
    nombre = models.CharField(
        max_length=60,
        verbose_name='Nombre',
        unique=True,
        null=False,
        blank=False)
    biografia = models.TextField(
        verbose_name='Biografía',
        max_length=4000,
        null=True,
        blank=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(
        max_length=60,
        verbose_name='Nombre',
        unique=True,
        null=False,
        blank=False)
    direcion = models.CharField(
        max_length=60,
        verbose_name='Dirección',
        null=True,
        blank=True)
    url = models.URLField(max_length=70)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(
        max_length=100,
        verbose_name='Título',
        unique=True,
        null=False,
        blank=False)
    descripcion = models.CharField(
        max_length=60,
        verbose_name='Descripción',
        null=True,
        blank=True)
    url = models.URLField(max_length=70)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.nombre