# Generated by Django 5.0.6 on 2024-07-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funkosapp', '0004_alter_funko_tenemos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funko',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('r', 'Recopilación'), ('n', 'No tenemos'), ('j', 'Juego')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
