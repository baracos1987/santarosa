# Generated by Django 4.1.7 on 2023-04-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0003_remove_tarifas_motos_cambio_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarifas_motos',
            name='descripcion_tarifa',
            field=models.CharField(default='Sin descripción', max_length=100),
        ),
    ]