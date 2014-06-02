# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0010_auto_20140602_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 2, 9, 17, 44, 710259), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 2, 9, 17, 44, 710349), auto_now_add=True),
        ),
    ]
