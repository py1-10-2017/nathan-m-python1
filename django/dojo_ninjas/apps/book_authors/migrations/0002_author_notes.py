# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=''),
        ),
    ]
