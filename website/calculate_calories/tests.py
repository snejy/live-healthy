from django.test import TestCase
from django.contrib.auth.models import User
from calculate_calories.models import UserProfile
from calculate_calories.helper import calories


class CalculatesCaloriesRight(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="mitka",
            password="pass",
            email="mitka@example.bg",
            first_name="Mitka",
            last_name="Mitka Mitka")
        balance = calories('f', 52,156, 22, 1.2)
        user_profile = UserProfile(
            user=user,
            gender='f',
            age=22,
            kilograms=52,
            height=156,
            sports=1.2,
            calorie_balance = balance)
        user_profile.save()

    def test_calculate_correctly(self):
        user = User.objects.get(username="Mitko")
        userprofile = UserProfile.objects.get(user=user)
        self.assertEqual(1597, userprofile.calorie_balance)
