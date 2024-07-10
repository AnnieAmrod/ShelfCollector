# Generated by Django 5.0.6 on 2024-07-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videojuego',
            name='formato',
            field=models.CharField(choices=[('d', 'Digital'), ('c', 'Código de descarga'), ('f', 'Físico'), ('p', 'Pirata')], default='f', max_length=20, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='nombre',
            field=models.CharField(max_length=60, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('j', 'Juego'), ('r', 'Recopilación'), ('n', 'No tenemos')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
        migrations.AlterUniqueTogether(
            name='videojuego',
            unique_together={('nombre', 'anio')},
        ),
    ]
