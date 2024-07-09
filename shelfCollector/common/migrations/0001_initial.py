# Generated by Django 5.0.6 on 2024-07-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carpeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name_plural': 'Carpetas',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('descripcion', models.TextField(blank=True, max_length=300, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name_plural': 'Géneros',
            },
        ),
    ]