# Generated by Django 5.0.6 on 2024-07-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funkosapp', '0003_alter_funko_tenemos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funko',
            name='tenemos',
            field=models.CharField(blank=True, choices=[('n', 'No tenemos'), ('j', 'Juego'), ('r', 'Recopilación')], default='j', max_length=1, null=True, verbose_name='Tenemos'),
        ),
    ]
