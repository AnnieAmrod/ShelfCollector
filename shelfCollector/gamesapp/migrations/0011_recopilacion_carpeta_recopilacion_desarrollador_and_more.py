# Generated by Django 5.0.6 on 2024-07-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_genero_options'),
        ('gamesapp', '0010_alter_edadrecomendada_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recopilacion',
            name='carpeta',
            field=models.ManyToManyField(blank=True, related_name='recopilaciones_carpetas', to='common.carpeta', verbose_name='Carpeta'),
        ),
        migrations.AddField(
            model_name='recopilacion',
            name='desarrollador',
            field=models.ManyToManyField(related_name='recopilaciones_desarrolladores', to='gamesapp.desarrollador', verbose_name='Desarrollador'),
        ),
        migrations.AddField(
            model_name='recopilacion',
            name='distribuidor',
            field=models.ManyToManyField(related_name='recopilaciones_distribuidores', to='gamesapp.distibuidor', verbose_name='Distribuidor'),
        ),
        migrations.AddField(
            model_name='recopilacion',
            name='genero',
            field=models.ManyToManyField(related_name='recopilaciones_generos', to='common.genero', verbose_name='Género'),
        ),
        migrations.AddField(
            model_name='recopilacion',
            name='modo_juego',
            field=models.ManyToManyField(related_name='recopilaciones_modos_juego', to='gamesapp.modo', verbose_name='Modo de Juego'),
        ),
        migrations.AddField(
            model_name='recopilacion',
            name='plataforma',
            field=models.ManyToManyField(related_name='recopilaciones_plataformas', to='gamesapp.plataforma', verbose_name='Plataforma'),
        ),
        migrations.AddField(
            model_name='recopilacion',
            name='programa',
            field=models.ManyToManyField(blank=True, related_name='recopilaciones_programa', to='gamesapp.tipocontenido', verbose_name='Programa'),
        ),
        migrations.AddField(
            model_name='recopilacion',
            name='tipo_contenido',
            field=models.ManyToManyField(blank=True, related_name='recopilaciones_tipo_contenido', to='gamesapp.tipocontenido', verbose_name='Tipo de Contenido'),
        ),
        migrations.AlterField(
            model_name='edadrecomendada',
            name='descripcion',
            field=models.CharField(max_length=200, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='recopilacion',
            name='formato',
            field=models.CharField(blank=True, choices=[('d', 'Digital'), ('f', 'Físico'), ('p', 'Pirata'), ('c', 'Código de descarga')], default='f', max_length=20, null=True, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='recopilacion',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('j', 'Juego'), ('r', 'Recopilación'), ('n', 'No tenemos')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='formato',
            field=models.CharField(blank=True, choices=[('d', 'Digital'), ('f', 'Físico'), ('p', 'Pirata'), ('c', 'Código de descarga')], default='f', max_length=20, null=True, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='programa',
            field=models.ManyToManyField(blank=True, related_name='videojuegos_programa', to='gamesapp.programa', verbose_name='Programa'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('j', 'Juego'), ('r', 'Recopilación'), ('n', 'No tenemos')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
