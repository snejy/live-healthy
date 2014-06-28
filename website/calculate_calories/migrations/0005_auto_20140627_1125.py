# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0004_auto_20140627_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_food',
            name='calories_consumated',
            field=models.PositiveIntegerField(default='0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='users_food',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, default=datetime.datetime(2014, 6, 27, 11, 25, 3, 909730)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True, default=datetime.datetime(2014, 6, 27, 11, 25, 3, 908341)),
        ),
    ]
