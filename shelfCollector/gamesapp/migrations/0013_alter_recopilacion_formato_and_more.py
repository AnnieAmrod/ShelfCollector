# Generated by Django 5.0.6 on 2024-07-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0012_alter_recopilacion_formato_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recopilacion',
            name='formato',
            field=models.CharField(blank=True, choices=[('d', 'Digital'), ('f', 'Físico'), ('c', 'Código de descarga'), ('p', 'Pirata')], default='f', max_length=20, null=True, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='recopilacion',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('r', 'Recopilación'), ('n', 'No tenemos'), ('j', 'Juego')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='formato',
            field=models.CharField(blank=True, choices=[('d', 'Digital'), ('f', 'Físico'), ('c', 'Código de descarga'), ('p', 'Pirata')], default='f', max_length=20, null=True, verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='videojuego',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('r', 'Recopilación'), ('n', 'No tenemos'), ('j', 'Juego')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
