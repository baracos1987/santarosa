# Generated by Django 4.1.7 on 2023-05-03 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0041_inicial_prenda_carro'),
    ]

    operations = [
        migrations.CreateModel(
            name='traspaso_prenda_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'traspaso_prenda_carro_parti',
                'verbose_name_plural': 'Requisitos Traspaso y Prenda Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='traslado_cuenta_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'traslado_cuenta_carro_parti',
                'verbose_name_plural': 'Requisitos Traslado de cuenta Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='polarizado_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'polarizado_carro_parti',
                'verbose_name_plural': 'Requisitos Polarizado Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='modifi_alerta_propi_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'modifi_alerta_propi_carro_parti',
                'verbose_name_plural': 'Requisitos Modificacion Alerta Propietario Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='modifi_alerta_acreedor_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'modifi_alerta_acreedor_carro_parti',
                'verbose_name_plural': 'Requisitos Modificacion Alerta Acreedor Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='inscripcion_RUNT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'Inscripcion_RUNT',
                'verbose_name_plural': 'Requisitos Inscripcion RUNT',
            },
        ),
        migrations.CreateModel(
            name='historial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'historial',
                'verbose_name_plural': 'Requisitos Historial',
            },
        ),
        migrations.CreateModel(
            name='expedicion_Licencia_Conduccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'Expedicion_Licencia_Conduccion',
                'verbose_name_plural': 'Requisitos Expedicion Licencia Conduccion',
            },
        ),
        migrations.CreateModel(
            name='cambio_documento2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'Cambio_Documento2',
                'verbose_name_plural': 'Requisitos Cambio Documento Mismo Número',
            },
        ),
        migrations.CreateModel(
            name='cambio_documento1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'Cambio_Documento1',
                'verbose_name_plural': 'Requisitos Cambio Documento Diferente Número',
            },
        ),
        migrations.CreateModel(
            name='cambio_conjunto_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'cambio_conjunto_carro_parti',
                'verbose_name_plural': 'Requisitos Cambio Conjunto Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='blindaje_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'blindaje_carro_parti',
                'verbose_name_plural': 'Requisitos Blindaje Carro Particular',
            },
        ),
        migrations.CreateModel(
            name='actualizacion_RUNT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'Actualizacion_RUNT',
                'verbose_name_plural': 'Requisitos Actualizacion RUNT',
            },
        ),
    ]