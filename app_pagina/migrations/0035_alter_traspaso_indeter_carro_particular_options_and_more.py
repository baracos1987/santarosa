# Generated by Django 4.1.7 on 2023-04-26 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0034_traspaso_indeter_carro_particular'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='traspaso_indeter_carro_particular',
            options={'verbose_name': 'indeterminado_carro_particular', 'verbose_name_plural': 'Requisitos Traspaso Indeterminado Carro Particular'},
        ),
        migrations.CreateModel(
            name='cancelacion_licencia_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'cancelacion_licencia_carro_particular',
                'verbose_name_plural': 'Requisitos Cancelacion licencia Carro Particular',
            },
        ),
    ]
