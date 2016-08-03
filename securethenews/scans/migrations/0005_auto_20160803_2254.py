# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-03 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0004_auto_20160803_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scan',
            old_name='added',
            new_name='timestamp',
        ),
        migrations.AddField(
            model_name='scan',
            name='enforces_https',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
