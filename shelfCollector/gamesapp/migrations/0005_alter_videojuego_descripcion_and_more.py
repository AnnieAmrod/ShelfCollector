# Generated by Django 5.0.6 on 2024-07-10 17:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0004_alter_videojuego_anio_alter_videojuego_carpeta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='descripcion',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='formato',
            field=models.CharField(blank=True, choices=[('c', 'Código de descarga'), ('d', 'Digital'), ('f', 'Físico'), ('p', 'Pirata')], default='f', max_length=20, null=True, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('r', 'Recopilación'), ('n', 'No tenemos'), ('j', 'Juego')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
