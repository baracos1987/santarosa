# Generated by Django 4.1.7 on 2023-04-26 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0037_rename_cancela_licen_deterio_carro_part_cancela_licen_deterio_carro_particular_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inscrip_levanta_prenda_carro_parti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'Inscrip_levanta_prenda_carro_parti',
                'verbose_name_plural': 'Requisitos Inscripcion o Levanta Prenda Carro Particular',
            },
        ),
    ]
