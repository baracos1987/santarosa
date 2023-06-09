# Generated by Django 4.1.7 on 2023-04-26 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0039_cambio_color_carro_parti'),
    ]

    operations = [
        migrations.CreateModel(
            name='transformacion_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'transformacion_carro_particular',
                'verbose_name_plural': 'Requisitos Transformacion Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='repotenciacion_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'repotenciacion_carro_particular',
                'verbose_name_plural': 'Requisitos Repotenciacion Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='radicado_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'radicado_carro_particular',
                'verbose_name_plural': 'Requisitos Radicado De CuentaCarro Particular',
            },
        ),
        migrations.CreateModel(
            name='duplicado_placas_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'duplicado_placas_carro_parti',
                'verbose_name_plural': 'Requisitos Duplicado Placa Carro particular',
            },
        ),
        migrations.CreateModel(
            name='cambio_servicio_parti_publico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'cambio_servicio_parti_publico',
                'verbose_name_plural': 'Requisitos Cambio Cambio Particular a Publico',
            },
        ),
        migrations.CreateModel(
            name='cambio_motor_regra_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'cambio_motor_regra_carro_parti',
                'verbose_name_plural': 'Requisitos Cambio Motor Regrabacion Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='cambio_motor_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'cambio_motor_carro_particular',
                'verbose_name_plural': 'Requisitos Cambio Motor Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='cambio_carroce_otro_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'cambio_carroce_otro_carro_particular',
                'verbose_name_plural': 'Requisitos cambio Carroceria otro vehiculo carro Particular',
            },
        ),
        migrations.CreateModel(
            name='cambio_carroce_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'cambio_carroce_carro_particular',
                'verbose_name_plural': 'Requisitos cambio Carroceria vehiculo carro Particular',
            },
        ),
    ]
