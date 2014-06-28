from django.contrib import admin
from calculate_calories.models import Temp, UserProfile, Food, Users_Food


class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'gender',
        'sports',
        'calorie_balance',
    ]

admin.site.register(UserProfile, UsersAdmin)


class FoodsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'food_name',
        'food_type',
        'calories_per_100gr',
    ]

admin.site.register(Food, FoodsAdmin)


class Users_FoodAdmin(admin.ModelAdmin):
    list_display = [
        'user_id',
        'food_id',
        'amount_of_food',
        'date',
        'calories_consumated',
    ]

admin.site.register(Users_Food, Users_FoodAdmin)


class TempAdmin(admin.ModelAdmin):
    list_display = [
        'food1',
        'food1_amount',
        'food2',
        'food2_amount',
    ]

admin.site.register(Temp, TempAdmin)