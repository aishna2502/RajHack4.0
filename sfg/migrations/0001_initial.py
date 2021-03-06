# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-09 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=250)),
                ('image', models.CharField(max_length=5000)),
                ('text', models.CharField(max_length=50000)),
                ('previous_hash', models.CharField(max_length=256)),
                ('hash', models.CharField(max_length=256)),
            ],
        ),
    ]
