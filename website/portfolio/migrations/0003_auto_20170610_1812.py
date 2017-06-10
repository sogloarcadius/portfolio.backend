# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20170610_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_es',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='description_fr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='summary_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='summary_es',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='summary_fr',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
