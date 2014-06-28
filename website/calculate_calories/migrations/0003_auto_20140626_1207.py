# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0002_auto_20140626_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_food',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, default=datetime.datetime(2014, 6, 26, 12, 7, 34, 831349)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, null=True, default=datetime.datetime(2014, 6, 26, 12, 7, 34, 830183)),
        ),
    ]
