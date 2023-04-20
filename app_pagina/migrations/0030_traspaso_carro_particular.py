# Generated by Django 4.1.7 on 2023-04-20 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pagina', '0029_alter_inicial_carro_particular_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='traspaso_carro_particular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requisitos_carro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_pagina.requisitos_tramites')),
            ],
            options={
                'verbose_name': 'traspaso_carro_particular',
                'verbose_name_plural': 'Requisitos Traspaso Carro Particular',
            },
        ),
    ]
