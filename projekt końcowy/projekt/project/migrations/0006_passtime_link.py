# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-12-19 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_categories_passtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='passtime',
            name='link',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]
