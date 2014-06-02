# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0003_auto_20140601_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 6, 1, 23, 47, 47, 298960)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 6, 1, 23, 47, 47, 298859)),
        ),
    ]
