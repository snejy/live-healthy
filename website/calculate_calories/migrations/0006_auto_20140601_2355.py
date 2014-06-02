# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0005_auto_20140601_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='admin', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 6, 1, 23, 55, 30, 75313)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 6, 1, 23, 55, 30, 75401)),
        ),
    ]
