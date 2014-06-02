# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0006_auto_20140601_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.PositiveIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 2, 1, 25, 5, 40619), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 2, 1, 25, 5, 40717), auto_now_add=True),
        ),
    ]
