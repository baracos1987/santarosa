# Generated by Django 4.1.7 on 2023-06-26 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0056_rematricula_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='transformacion_moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'transformacion_moto',
                'verbose_name_plural': 'Requisitos Transformacion Moto',
            },
        ),
        migrations.CreateModel(
            name='modificar_alerta_prop_moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'modificar_alerta_prop_moto',
                'verbose_name_plural': 'Requisitos Modificar Alerta Propietario Moto',
            },
        ),
        migrations.CreateModel(
            name='indeterminado_moto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'indeterminado_moto',
                'verbose_name_plural': 'Requisitos Traspaso Indeterminado Moto',
            },
        ),
    ]
