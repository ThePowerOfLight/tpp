# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-04-25 06:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Viewer', '0004_auto_20190221_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewerorder',
            name='v_expire',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 25, 14, 21, 22, 670065)),
        ),
    ]