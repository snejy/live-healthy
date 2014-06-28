# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0003_auto_20140626_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_food',
            name='date',
            field=models.DateTimeField(null=True, default=datetime.datetime(2014, 6, 27, 10, 4, 11, 456420), auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users_food',
            name='user_id',
            field=models.ForeignKey(to_field='id', to='calculate_calories.UserProfile'),
        ),
        migrations.AlterField(
            model_name='users_food',
            name='food_id',
            field=models.ForeignKey(to_field='id', to='calculate_calories.Food'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(null=True, default=datetime.datetime(2014, 6, 27, 10, 4, 11, 455377), auto_now_add=True),
        ),
    ]
