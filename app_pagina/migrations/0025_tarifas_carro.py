# Generated by Django 4.1.7 on 2023-04-18 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0024_alter_tarifas_motos_valor_tarifa_runt'),
    ]

    operations = [
        migrations.CreateModel(
            name='tarifas_carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_tarifa', models.CharField(max_length=100, verbose_name='Descripcion Tarifa')),
                ('valor_tarifa', models.IntegerField(verbose_name='Valor Tarifa TTO')),
                ('valor_tarifa_RUNT', models.IntegerField(verbose_name='Valor Tarifa RUNT')),
                ('valor_total', models.IntegerField(blank=True, default=0, editable=False, verbose_name='Valor Total')),
                ('año', models.CharField(blank=True, max_length=100, verbose_name='año tarifa')),
            ],
        ),
    ]
