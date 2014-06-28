# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0005_auto_20140627_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Temp',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('food1', models.TextField()),
                ('food2', models.TextField()),
                ('food1_amount', models.PositiveIntegerField()),
                ('food2_amount', models.PositiveIntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 6, 27, 21, 58, 18, 683502), null=True, auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 27, 21, 58, 18, 681762), null=True, auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='users_food',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 6, 27, 21, 58, 18, 682923), null=True, auto_now_add=True),
        ),
    ]
