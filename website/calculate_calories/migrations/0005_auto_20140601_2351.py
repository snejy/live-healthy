# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0004_auto_20140601_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 6, 1, 23, 51, 44, 758624)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2014, 6, 1, 23, 51, 44, 758714)),
        ),
    ]
