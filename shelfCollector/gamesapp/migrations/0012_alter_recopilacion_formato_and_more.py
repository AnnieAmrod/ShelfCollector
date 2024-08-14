# Generated by Django 5.0.6 on 2024-07-28 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0011_recopilacion_carpeta_recopilacion_desarrollador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recopilacion',
            name='formato',
            field=models.CharField(blank=True, choices=[('p', 'Pirata'), ('c', 'Código de descarga'), ('f', 'Físico'), ('d', 'Digital')], default='f', max_length=20, null=True, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='recopilacion',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('n', 'No tenemos'), ('j', 'Juego'), ('r', 'Recopilación')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='coleccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gamesapp.coleccion', verbose_name='Colección'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='formato',
            field=models.CharField(blank=True, choices=[('p', 'Pirata'), ('c', 'Código de descarga'), ('f', 'Físico'), ('d', 'Digital')], default='f', max_length=20, null=True, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='img',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('n', 'No tenemos'), ('j', 'Juego'), ('r', 'Recopilación')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
