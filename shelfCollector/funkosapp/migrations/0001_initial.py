# Generated by Django 5.0.6 on 2024-07-10 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0002_alter_genero_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=4000, null=True, verbose_name='Descripcion')),
                ('url', models.URLField(max_length=70)),
            ],
            options={
                'verbose_name': 'Colección',
                'verbose_name_plural': 'Colecciones',
            },
        ),
        migrations.CreateModel(
            name='Tamano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=4000, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tamaño',
                'verbose_name_plural': 'Tamaños',
            },
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=4000, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.CreateModel(
            name='Funko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_coleccion', models.CharField(max_length=5, verbose_name='Número de Colección')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre')),
                ('img', models.CharField(blank=True, max_length=40, null=True, verbose_name='Imagen')),
                ('serie', models.CharField(blank=True, max_length=40, null=True, verbose_name='Serie')),
                ('num_serie', models.CharField(blank=True, max_length=40, null=True, verbose_name='Número de Serie')),
                ('tenemos', models.CharField(blank=True, choices=[('r', 'Recopilación'), ('j', 'Juego'), ('n', 'No tenemos')], default='j', max_length=1, null=True, verbose_name='Tenemos')),
                ('wish_list', models.BooleanField(default=False, verbose_name='Wish List')),
                ('carpeta', models.ManyToManyField(blank=True, related_name='funkos_carpetas', to='common.carpeta', verbose_name='Carpeta')),
                ('coleccion', models.ManyToManyField(related_name='funko_colecciones', to='funkosapp.coleccion', verbose_name=' Colección')),
                ('genero', models.ManyToManyField(related_name='funko_generos', to='common.genero', verbose_name=' Género')),
                ('tamano', models.ManyToManyField(blank=True, related_name='funko_tamanos', to='funkosapp.tamano', verbose_name=' Tamaño')),
                ('tipo', models.ManyToManyField(blank=True, related_name='funko_tipos', to='funkosapp.tipo', verbose_name=' Tipo')),
            ],
            options={
                'verbose_name': 'Funko',
                'verbose_name_plural': 'Funkos',
                'unique_together': {('n_coleccion', 'nombre')},
            },
        ),
    ]
