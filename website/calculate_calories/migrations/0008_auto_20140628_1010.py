# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0007_auto_20140627_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(null=True, default=datetime.datetime(2014, 6, 28, 10, 10, 19, 344083), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='temp',
            name='date',
            field=models.DateTimeField(null=True, default=datetime.datetime(2014, 6, 28, 10, 10, 19, 345882), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users_food',
            name='date',
            field=models.DateTimeField(null=True, default=datetime.datetime(2014, 6, 28, 10, 10, 19, 345284), auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together=set([('food_name', 'food_type')]),
        ),
    ]
