# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]