from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import UserManager
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(default = 'admin',max_length = 30)
    email = models.EmailField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    GENDER = (
        ('f', 'female'),
        ('m', 'male')
    )
    gender = models.CharField(max_length = 1,
                              choices = GENDER,
                              default = 'f')
    # date_of_birth = models.DateField(blank = False)
    age = models.PositiveIntegerField(null = True)
    kilograms = models.PositiveIntegerField(null = True)
    height = models.PositiveIntegerField(null = True)
    SPORTS = (
        (1.2, "Does not do sport."),
        (1.375, "Does sport 1 to 3 times weekly."),
        (1.55, "Does sport 3 to 5 times weekly."),
        (1.725, "Does sport 6 to 7 times weekly."),
        (1.9, "Extreme active: 7 times weekly with additional activities.")
    )
    sports = models.FloatField(null = True, choices = SPORTS )
    calorie_balance = models.PositiveIntegerField(default = 0)
    objects = UserManager()

    def __unicode__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.id = existing.id #force update instead of insert
        except UserProfile.DoesNotExist:
            pass 
        models.Model.save(self, *args, **kwargs)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)