# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-03 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='pic',
            field=models.ImageField(default='foo.img', upload_to=''),
            preserve_default=False,
        ),
    ]
