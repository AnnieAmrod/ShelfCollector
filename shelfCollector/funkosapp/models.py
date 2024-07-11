from django.db import models
from common.models import Genero, Carpeta


# Create your models here.
class Coleccion(models.Model):
    nombre = models.CharField(
                            max_length=60,
                            verbose_name='Nombre',
                            unique=True,
                            null=False,
                            blank=False)
    descripcion = models.TextField(
                            verbose_name='Descripcion',
                            max_length=4000,
                            null=True,
                            blank=True)
    url = models.URLField(max_length=70)

    class Meta:
        verbose_name = 'Colección'
        verbose_name_plural = 'Colecciones'

    def __str__(self):
        return self.nombre


class Tamano(models.Model):
    nombre = models.CharField(
                            max_length=60,
                            verbose_name='Nombre',
                            unique=True,
                            null=False,
                            blank=False)
    descripcion = models.TextField(
                            verbose_name='Descripcion',
                            max_length=4000,
                            null=True,
                            blank=True)

    class Meta:
        verbose_name = 'Tamaño'
        verbose_name_plural = 'Tamaños'

    def __str__(self):
        return self.nombre


class Tipo(models.Model):
    nombre = models.CharField(
                            max_length=60,
                            verbose_name='Nombre',
                            unique=True,
                            null=False,
                            blank=False)
    descripcion = models.TextField(
                            verbose_name='Descripcion',
                            max_length=4000,
                            null=True,
                            blank=True)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nombre


class Funko(models.Model):
    SI = 'j'
    NO = 'n'
    RECOPILACION = 'r'
    TENEMOS_CHOICES = {
        (SI, 'Juego'),
        (NO, 'No tenemos'),
        (RECOPILACION, 'Recopilación'),
    }

    n_coleccion = models.CharField(
                            max_length=5,
                            verbose_name='Número de Colección',
                            null=False,
                            blank=False)
    nombre = models.CharField(
                            max_length=60,
                            verbose_name='Nombre',
                            null=False,
                            blank=False)
    img = models.CharField(
                            max_length=40,
                            verbose_name='Imagen',
                            blank=True,
                            null=True)
    coleccion = models.ManyToManyField(
                            Coleccion,
                            verbose_name=' Colección',
                            blank=False,
                            related_name='funko_colecciones')
    serie = models.CharField(
                            max_length=40,
                            verbose_name='Serie',
                            blank=True,
                            null=True)
    tamano = models.ManyToManyField(
                            Tamano,
                            verbose_name=' Tamaño',
                            blank=True,
                            related_name='funko_tamanos')
    tipo = models.ManyToManyField(
                            Tipo,
                            verbose_name=' Tipo',
                            blank=True,
                            related_name='funko_tipos')
    genero = models.ManyToManyField(
                            Genero,
                            verbose_name=' Género',
                            blank=False,
                            related_name='funko_generos')
    num_serie = models.CharField(
                            max_length=40,
                            verbose_name='Número de Serie',
                            blank=True,
                            null=True)
    tenemos = models.CharField(
                            max_length=1,
                            verbose_name='Tenemos',
                            choices=TENEMOS_CHOICES,
                            default=SI,
                            blank=True,
                            null=True)
    wish_list = models.BooleanField(
                            verbose_name='Wish List',
                            default=False)
    carpeta = models.ManyToManyField(
                            Carpeta,
                            verbose_name='Carpeta',
                            blank=True,
                            related_name='funkos_carpetas')

    class Meta:
        verbose_name = 'Funko'
        verbose_name_plural = 'Funkos'
        unique_together = ['n_coleccion', 'nombre']

    def __str__(self):
        return self.nombre
