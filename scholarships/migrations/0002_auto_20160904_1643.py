# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-04 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='count',
            field=models.PositiveIntegerField(null=True, verbose_name='Number of Awards (blank if unknown)'),
        ),
        migrations.AlterField(
            model_name='scholarship',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
