from django.db import models

# Create your models here.
from common.models import Genero, Carpeta
from ckeditor.fields import RichTextField


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
    url = models.URLField(max_length=70)

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
    direccion = models.CharField(
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


class Idioma(models.Model):
    nombre = models.CharField(
                            max_length=60,
                            verbose_name='Nombre',
                            unique=True,
                            null=False,
                            blank=False)

    class Meta:
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    SI = 'j'
    NO = 'n'
    RECOPILACION = 'r'
    TENEMOS_CHOICES = {
        (SI, 'Juego'),
        (NO, 'No tenemos'),
        (RECOPILACION, 'Recopilación'),
    }

    titulo = models.CharField(
                            max_length=100,
                            verbose_name='Título',
                            unique=True,
                            null=False,
                            blank=False)
    # descripcion = models.CharField(
    #                        max_length=4000,
    #                        verbose_name='Descripción',
    #                        null=True,
    #                        blank=True)
    descripcion = RichTextField(max_length=4000, verbose_name='Descripción', null=True, blank=True)
    fecha_publicacion = models.DateField(
                            auto_now=False,
                            auto_now_add=False,
                            verbose_name='Fecha de Publicación',
                            null=True,
                            blank=True)
    portada = models.CharField(
                            max_length=40,
                            verbose_name='Portada',
                            blank=True,
                            null=True)
    autor = models.ManyToManyField(
                            Autor,
                            verbose_name='Autor',
                            blank=False,
                            related_name='libro_autores')
    genero = models.ManyToManyField(
                            Genero,
                            verbose_name='Genero',
                            blank=False,
                            related_name='libro_generos')
    editorial = models.ManyToManyField(
                            Editorial,
                            verbose_name='Editorial',
                            blank=False,
                            related_name='libro_editoriales')
    isbn = models.CharField(
                            max_length=13,
                            verbose_name='ISBN',
                            blank=True,
                            null=True)
    fecha_leido = models.DateField(
                            auto_now=False,
                            auto_now_add=False,
                            verbose_name='Fecha de leído',
                            null=True,
                            blank=True)
    leido_por = models.CharField(
                            max_length=30,
                            verbose_name='Leído por',
                            blank=True,
                            null=True)
    precio = models.CharField(
                            max_length=30,
                            verbose_name='Precio',
                            blank=True,
                            null=True)
    paginas = models.CharField(
                            max_length=4,
                            verbose_name='Páginas',
                            blank=True,
                            null=True)
    idioma = models.ManyToManyField(
                            Idioma,
                            verbose_name='Idioma',
                            blank=False,
                            related_name='libro_idiomas')
    carpeta = models.ManyToManyField(
                            Carpeta,
                            verbose_name='Carpeta',
                            blank=False,
                            related_name='libros_carpeta')
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

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo
