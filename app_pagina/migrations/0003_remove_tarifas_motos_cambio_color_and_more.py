# Generated by Django 4.1.7 on 2023-04-14 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0002_remove_tarifas_motos_historial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='cambio_color',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='cambio_motor',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='cancelacion_lt',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='duplicado_lt',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='duplicado_placa',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='inicial_prenda',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='inscripcion_prenda',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='levante_prenda',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='mod_alerta_acree',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='mod_alerta_propi',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='radicado_cuenta',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='re_matricula',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='regrabacion',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='traslado_cuenta',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='traspaso',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='traspaso_indeter',
        ),
        migrations.RemoveField(
            model_name='tarifas_motos',
            name='traspaso_prenda',
        ),
    ]
