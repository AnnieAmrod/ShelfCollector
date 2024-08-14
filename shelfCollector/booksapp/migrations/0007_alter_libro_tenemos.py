# Generated by Django 5.0.6 on 2024-07-23 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksapp', '0006_alter_libro_tenemos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('n', 'No tenemos'), ('j', 'Juego'), ('r', 'Recopilación')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
