# Generated by Django 4.1.7 on 2023-06-26 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0045_traspaso_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='traspaso_moto_prensa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_moto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'traspaso_moto_prensa',
                'verbose_name_plural': 'Requisitos Traspaso Moto Con Prenda',
            },
        ),
    ]
