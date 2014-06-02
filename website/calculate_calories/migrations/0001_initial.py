# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('email', models.EmailField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(default='f', choices=[('f', 'female'), ('m', 'male')], max_length=1)),
                ('kilograms', models.PositiveIntegerField(null=True)),
                ('height', models.PositiveIntegerField(null=True)),
                ('sports', models.FloatField(choices=[(1.2, 'Does not do sport.'), (1.375, 'Does sport 1 to 3 times weekly.'), (1.55, 'Does sport 3 to 5 times weekly.'), (1.725, 'Does sport 6 to 7 times weekly.'), (1.9, 'Extreme active: 7 times weekly with additional activities.')], null=True)),
                ('calorie_balance', models.PositiveIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
