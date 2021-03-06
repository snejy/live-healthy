from datetime import datetime

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User, UserManager


class UserProfile(models.Model):
    FEMALE = 'f'
    MALE = 'm'
    GENDER = (
        (FEMALE, 'female'),
        (MALE, 'male')
    )
    SPORTS = (
        (1.2, "Does not do sport."),
        (1.375, "Does sport 1 to 3 times weekly."),
        (1.55, "Does sport 3 to 5 times weekly."),
        (1.725, "Does sport 6 to 7 times weekly."),
        (1.9, "Extreme active: 7 times weekly with additional activities.")
    )
    user = models.OneToOneField(User)
    gender = models.CharField(max_length=1,
                              choices=GENDER,
                              default=FEMALE)
    age = models.PositiveIntegerField(null=True)
    kilograms = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    sports = models.FloatField(choices=SPORTS, default = SPORTS[0][0])
    calorie_balance = models.PositiveIntegerField(default=0)
    date_joined = models.DateTimeField(default=datetime.now(),
                                       auto_now_add=True,
                                       null=True)
    objects = UserManager()

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
    name = models.TextField(blank=False)
    foodtype = models.TextField(blank=False)
    #  calories in 100 gr food
    calories_per_100gr = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'foodtype'),)


class Consumation(models.Model):
    user = models.ForeignKey(UserProfile, related_name='consumation')
    food = models.ForeignKey(Food, related_name='consumation')
    amount_of_food = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    calories_consumated = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{} - {} calories in {} grams.".format(self.food_id, self.calories_consumated, self.amount_of_food)


class Temp(models.Model):
    food1 = models.TextField(default='')
    food2 = models.TextField(default='')
    food1_amount = models.PositiveIntegerField(blank=False, default=0)
    food2_amount = models.PositiveIntegerField(blank=False, default=0)
    date = models.DateTimeField(default=datetime.now(),
                                auto_now_add=True,
                                null=True)

    def __str__(self):
        return str(self.food1) + " - " + str(self.food1_amount) + " and " + str(self.food2) + " - " + str(self.food2_amount)

    class Meta:
        unique_together= (('food1', 'food2', 'food1_amount', 'food2_amount'),)