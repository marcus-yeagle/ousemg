# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20160504_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
