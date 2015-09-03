# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('calculate_calories', '0008_auto_20140628_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_of_food', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('calories_consumated', models.PositiveIntegerField(default=0)),
                ('food', models.ForeignKey(related_name='consumation', to='calculate_calories.Food')),
                ('user', models.ForeignKey(related_name='consumation', to='calculate_calories.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='users_food',
            name='food_id',
        ),
        migrations.RemoveField(
            model_name='users_food',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='Users_Food',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food_name',
            new_name='foodtype',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='food_type',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='food',
            name='calories_per_100gr',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='temp',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 21, 17, 34, 960697), auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='temp',
            name='food1',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='temp',
            name='food2',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 1, 21, 17, 34, 954268), auto_now_add=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sports',
            field=models.FloatField(default=1.2, choices=[(1.2, b'Does not do sport.'), (1.375, b'Does sport 1 to 3 times weekly.'), (1.55, b'Does sport 3 to 5 times weekly.'), (1.725, b'Does sport 6 to 7 times weekly.'), (1.9, b'Extreme active: 7 times weekly with additional activities.')]),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together=set([('name', 'foodtype')]),
        ),
    ]
