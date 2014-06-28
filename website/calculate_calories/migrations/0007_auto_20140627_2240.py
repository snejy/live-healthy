# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0006_auto_20140627_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='food1',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='temp',
            name='food2',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='temp',
            name='food1_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='temp',
            name='food2_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='temp',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 27, 22, 40, 43, 342939), auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='users_food',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 27, 22, 40, 43, 342331), auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 27, 22, 40, 43, 341057), auto_now_add=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='temp',
            unique_together=set([('food1', 'food2', 'food1_amount', 'food2_amount')]),
        ),
    ]
