# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-09 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mushrooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('geom', djgeojson.fields.PolygonField()),
            ],
        ),
    ]
