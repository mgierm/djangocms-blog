# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_blog', '0034_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttranslation',
            name='subtitle',
            field=models.TextField(blank=True, default='', verbose_name='subtitle'),
        ),
    ]
