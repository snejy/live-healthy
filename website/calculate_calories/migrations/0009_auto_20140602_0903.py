# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0008_auto_20140602_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 2, 9, 3, 35, 479964), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 2, 9, 3, 35, 479874), auto_now_add=True),
        ),
    ]
