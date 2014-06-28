from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import UserManager
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    GENDER = (
        ('f', 'female'),
        ('m', 'male')
    )
    gender = models.CharField(max_length=1,
                              choices=GENDER,
                              default='f')
    age = models.PositiveIntegerField(null=True)
    kilograms = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    SPORTS = (
        (1.2, "Does not do sport."),
        (1.375, "Does sport 1 to 3 times weekly."),
        (1.55, "Does sport 3 to 5 times weekly."),
        (1.725, "Does sport 6 to 7 times weekly."),
        (1.9, "Extreme active: 7 times weekly with additional activities.")
    )
    sports = models.FloatField(null=True, choices=SPORTS)
    calorie_balance = models.PositiveIntegerField(default=0)
    date_joined = models.DateTimeField(default=datetime.now(),
                                       auto_now_add=True,
                                       null=True)
    objects = UserManager()

    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.id = existing.id  # force update instead of insert
        except UserProfile.DoesNotExist:
            pass
        models.Model.save(self, *args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Food(models.Model):
    food_name = models.TextField(blank=False)
    food_type = models.TextField(blank=False)
    #  calories in 100 gr food
    calories_per_100gr = models.PositiveIntegerField(blank=False,
                                                     default='0')

    def __unicode__(self):
        return self.food_name

    def __str__(self):
        return self.food_name

    class Meta:
        unique_together = (('food_name', 'food_type'),)


class Users_Food(models.Model):
    user_id = models.ForeignKey(UserProfile, related_name='userprofile_id')
    food_id = models.ForeignKey(Food, related_name='food_id')
    amount_of_food = models.PositiveIntegerField(blank=False, default='0')
    date = models.DateTimeField(default=datetime.now(),
                                auto_now_add=True,
                                null=True)
    calories_consumated = models.PositiveIntegerField(blank=False, default='0')

    def __str__(self):
        return str(self.food_id) + " - " + str(self.calories_consumated) + " calories in " + str(self.amount_of_food) + " grams."


class Temp(models.Model):
    food1 = models.TextField(blank=False, default='null')
    food2 = models.TextField(blank=False, default='null')
    food1_amount = models.PositiveIntegerField(blank=False, default=0)
    food2_amount = models.PositiveIntegerField(blank=False, default=0)
    date = models.DateTimeField(default=datetime.now(),
                                auto_now_add=True,
                                null=True)

    def __str__(self):
        return str(self.food1) + " - " + str(self.food1_amount) + " and " + str(self.food2) + " - " + str(self.food2_amount)

    class Meta:
        unique_together= (('food1', 'food2', 'food1_amount', 'food2_amount'),)