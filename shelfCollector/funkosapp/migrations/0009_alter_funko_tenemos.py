# Generated by Django 5.0.6 on 2024-07-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funkosapp', '0008_alter_funko_tenemos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funko',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('n', 'No tenemos'), ('r', 'Recopilación'), ('j', 'Juego')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
