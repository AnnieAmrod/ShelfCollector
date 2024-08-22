from django.db import models

# Create your models here.
# from shelfCollector.common.models import Genero
from common.models import Genero, Carpeta
from usuario.models import Usuario
from ckeditor.fields import RichTextField


class Distibuidor(models.Model):
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
        verbose_name = 'Distibuidor'
        verbose_name_plural = 'Distibuidores'

    def __str__(self):
        return self.nombre


class Desarrollador(models.Model):
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
        verbose_name = 'Desarrollador'
        verbose_name_plural = 'Desarrolladores'

    def __str__(self):
        return self.nombre


class Modo(models.Model):
    modo_juego = models.CharField(
                            max_length=25,
                            verbose_name='Modo de juego',
                            unique=True,
                            null=False,
                            blank=False)

    class Meta:
        verbose_name = 'Modo de Juego'
        verbose_name_plural = 'Modos de Juego'

    def __str__(self):
        return self.modo_juego


class Plataforma(models.Model):
    nombre = models.CharField(
                            max_length=10,
                            verbose_name='Plataforma',
                            unique=True,
                            null=False,
                            blank=False)
    retrocompatible = models.BooleanField(
                            verbose_name='Retrocompatible',
                            default=False)

    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'

    def __str__(self):
        return self.nombre


class EdadRecomendada(models.Model):
    numero = models.CharField(
                            max_length=2,
                            verbose_name='Número',
                            unique=True,
                            null=False,
                            blank=False)
    color = models.CharField(
                            max_length=8,
                            verbose_name='Color',
                            null=False,
                            blank=False)
    descripcion = models.TextField(
                            max_length=200,
                            verbose_name='Descripción',
                            #unique=True,
                            null=False,
                            blank=False)

    class Meta:
        verbose_name = 'Edad Recomendada'
        verbose_name_plural = 'Edades Recomendadas'

    def __str__(self):
        return f'PEGI {self.numero} (color {self.color.lower()})'


class TipoContenido(models.Model):
    nombre = models.CharField(
                            max_length=80,
                            verbose_name='Tipo de Contenido',
                            unique=True,
                            null=False,
                            blank=False)

    class Meta:
        verbose_name = 'Tipo de contenido'
        verbose_name_plural = 'Tipos de contenido'

    def __str__(self):
        return self.nombre


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


class Programa(models.Model):
    nombre = models.CharField(
                            max_length=10,
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
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    def __str__(self):
        return self.nombre


class Videojuego(models.Model):
    SI = 'j'
    NO = 'n'
    RECOPILACION = 'r'
    TENEMOS_CHOICES = {
        (SI, 'Juego'),
        (NO, 'No tenemos'),
        (RECOPILACION, 'Recopilación'),
    }

    FISICO = 'f'
    DIGITAL = 'd'
    PIRATA = 'p'
    CODIGO_DESCARGA = 'c'
    FORMATO_CHOICES = {
        (FISICO, 'Físico'),
        (DIGITAL, 'Digital'),
        (PIRATA, 'Pirata'),
        (CODIGO_DESCARGA, 'Código de descarga'),
    }

    nombre = models.CharField(
                            max_length=60,
                            verbose_name='Nombre',
                            #unique=True,
                            null=False,
                            blank=False)
    descripcion = models.TextField(
                            max_length=4000,
                            verbose_name='Descripción',
                            help_text='La encontrarás tras la portada',
                            null=True,
                            blank=True)
    sinopsis = RichTextField(max_length=4000, verbose_name='Sinopsis', help_text='Sinopsis (con spoilers) del juego', null=True, blank=True)
    # sinopsis = models.TextField(
    #                        verbose_name='Sinopsis',
    #                        max_length=4000,
    #                        null=True,
    #                        blank=True)
    anio = models.CharField(
                            max_length=4,
                            verbose_name='Año de publicación',
                            blank=False,
                            null=False)
    img = models.CharField(
                            max_length=100,
                            verbose_name='Imagen',
                            blank=True,
                            null=True)
    distribuidor = models.ManyToManyField(
                            Distibuidor,
                            verbose_name='Distribuidor',
                            blank=False,
                            related_name='videojuegos_distribuidores')
    desarrollador = models.ManyToManyField(
                            Desarrollador,
                            verbose_name='Desarrollador',
                            blank=False,
                            related_name='videojuegos_desarrolladores')
    modo_juego = models.ManyToManyField(
                            Modo,
                            verbose_name='Modo de Juego',
                            blank=False,
                            related_name='videojuegos_modos_juego')
    genero = models.ManyToManyField(
                            Genero,
                            verbose_name='Género',
                            blank=False,
                            related_name='videojuegos_generos')
    plataforma = models.ManyToManyField(
                            Plataforma,
                            verbose_name='Plataforma',
                            blank=False,
                            related_name='videojuegos_plataformas')
    precio = models.CharField(
                            max_length=6,
                            verbose_name='Precio',
                            blank=True,
                            null=True)
    edad_recomendada = models.ForeignKey(
                            EdadRecomendada,
                            verbose_name='Edad Recomendada',
                            on_delete=models.CASCADE,
                            null=False,
                            blank=False)
    tipo_contenido = models.ManyToManyField(
                            TipoContenido,
                            verbose_name='Tipo de Contenido',
                            blank=True,
                            related_name='videojuegos_tipo_contenido')
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
    coleccion = models.ForeignKey(
                            Coleccion,
                            verbose_name='Colección',
                            on_delete=models.PROTECT,
                            null=True,
                            blank=True)
    formato = models.CharField(
                            max_length=20,
                            verbose_name='Formato',
                            choices=FORMATO_CHOICES,
                            default=FISICO,
                            null=True,
                            blank=True)
    programa = models.ManyToManyField(
                            Programa,
                            verbose_name='Programa',
                            blank=True,
                            related_name='videojuegos_programa')
    carpeta = models.ManyToManyField(
                            Carpeta,
                            verbose_name='Carpeta',
                            blank=True,
                            related_name='videojuegos_carpetas')
    usuario = models.ForeignKey(
                            Usuario,
                            verbose_name='Usuario',
                            on_delete=models.PROTECT,
                            null=False,
                            blank=False)

    class Meta:
        verbose_name = 'Videojuego'
        verbose_name_plural = 'Videojuegos'
        unique_together = ['nombre', 'anio']

    def __str__(self):
        return self.nombre


class Recopilacion(models.Model):
    SI = 'j'
    NO = 'n'
    RECOPILACION = 'r'
    TENEMOS_CHOICES = {
        (SI, 'Juego'),
        (NO, 'No tenemos'),
        (RECOPILACION, 'Recopilación'),
    }

    FISICO = 'f'
    DIGITAL = 'd'
    PIRATA = 'p'
    CODIGO_DESCARGA = 'c'
    FORMATO_CHOICES = {
        (FISICO, 'Físico'),
        (DIGITAL, 'Digital'),
        (PIRATA, 'Pirata'),
        (CODIGO_DESCARGA, 'Código de descarga'),
    }

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
    # sinopsis = RichTextField(max_length=4000, verbose_name='Sinopsis', null=True, blank=True)
    sinopsis = models.TextField(
                            verbose_name='Sinopsis',
                            max_length=10000,
                            null=True,
                            blank=True)
    anio = models.CharField(
                            max_length=4,
                            verbose_name='Año de publicación',
                            blank=False,
                            null=True)
    img = models.CharField(
                            max_length=40,
                            verbose_name='Imagen',
                            blank=True,
                            null=True)
    distribuidor = models.ManyToManyField(
                            Distibuidor,
                            verbose_name='Distribuidor',
                            blank=False,
                            related_name='recopilaciones_distribuidores')
    desarrollador = models.ManyToManyField(
                            Desarrollador,
                            verbose_name='Desarrollador',
                            blank=False,
                            related_name='recopilaciones_desarrolladores')
    modo_juego = models.ManyToManyField(
                            Modo,
                            verbose_name='Modo de Juego',
                            blank=False,
                            related_name='recopilaciones_modos_juego')
    genero = models.ManyToManyField(
                            Genero,
                            verbose_name='Género',
                            blank=False,
                            related_name='recopilaciones_generos')
    plataforma = models.ManyToManyField(
                            Plataforma,
                            verbose_name='Plataforma',
                            blank=False,
                            related_name='recopilaciones_plataformas')
    precio = models.CharField(
                            max_length=6,
                            verbose_name='Precio',
                            blank=True,
                            null=True)
    edad_recomendada = models.ForeignKey(
                            EdadRecomendada,
                            verbose_name='Edad Recomendada',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=False)
    tipo_contenido = models.ManyToManyField(
                            TipoContenido,
                            verbose_name='Tipo de Contenido',
                            blank=True,
                            related_name='recopilaciones_tipo_contenido')
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
    coleccion = models.ForeignKey(
                            Coleccion,
                            verbose_name='Colección',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True)
    formato = models.CharField(
                            max_length=20,
                            verbose_name='Formato',
                            choices=FORMATO_CHOICES,
                            default=FISICO,
                            null=True,
                            blank=True)
    programa = models.ManyToManyField(
                            Programa,
                            verbose_name='Programa',
                            blank=True,
                            related_name='recopilaciones_programa')
    carpeta = models.ManyToManyField(
                            Carpeta,
                            verbose_name='Carpeta',
                            blank=True,
                            related_name='recopilaciones_carpetas')
    videojuegos = models.ManyToManyField(
                            Videojuego,
                            verbose_name='Videojuegos', related_name='recopilaciones')

    class Meta:
        verbose_name = 'Recopilación'
        verbose_name_plural = 'Recopilaciones'
        unique_together = ['nombre', 'anio']

    def save(self, *args, **kwargs):
        if not self.pk:  # Solo calcular la sinopsis al crear la instancia, no al actualizar
            self.sinopsis = self.generate_combined_sinopsis()
        super().save(*args, **kwargs)

    def generate_combined_sinopsis(self):
        sinopsis_list = self.videojuegos.values_list('sinopsis', flat=True)
        combined_sinopsis = " ".join(sinopsis_list)
        if len(combined_sinopsis) > 10000:
            combined_sinopsis = combined_sinopsis[:10000]  # Truncate to 10000 characters if necessary
        return combined_sinopsis

    def __str__(self):
        return self.nombre
