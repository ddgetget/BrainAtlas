# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-19 01:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='book', verbose_name='图片'),
        ),
    ]
