# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 17:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(help_text='T\xfa comentario', verbose_name='Comentario')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, unique=True, verbose_name='T\xedtulo')),
                ('ingredientes', models.TextField(help_text='Redacta los ingredientes')),
                ('preparacion', models.TextField(help_text='El proceso de preparaci\xf3n', verbose_name='Preparaci\xf3n')),
                ('imagen', models.ImageField(upload_to='recetas', verbose_name='Im\xe1gen')),
                ('tiempo_registro', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recetas.Receta'),
        ),
    ]
