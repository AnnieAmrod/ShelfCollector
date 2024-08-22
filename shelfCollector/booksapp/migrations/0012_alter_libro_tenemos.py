# Generated by Django 5.0.6 on 2024-07-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0011_alter_libro_tenemos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('j', 'Juego'), ('n', 'No tenemos'), ('r', 'Recopilación')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]