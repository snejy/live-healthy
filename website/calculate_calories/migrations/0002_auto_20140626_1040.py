# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('food_name', models.TextField()),
                ('food_type', models.TextField()),
                ('calories_per_100gr', models.PositiveIntegerField(default='0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users_Food',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user_id', models.OneToOneField(to='calculate_calories.UserProfile', to_field='id')),
                ('food_id', models.OneToOneField(to='calculate_calories.Food', to_field='id')),
                ('amount_of_food', models.PositiveIntegerField(default='0')),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 6, 26, 10, 40, 0, 222644), null=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 26, 10, 40, 0, 221539), null=True, auto_now_add=True),
        ),
    ]
