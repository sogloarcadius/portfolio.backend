# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(max_length=250),
        ),
    ]
