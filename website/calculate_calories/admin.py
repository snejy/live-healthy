from django.contrib import admin
from calculate_calories.models import Temp, UserProfile, Food, Consumation


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
        'name',
        'foodtype',
        'calories_per_100gr',
    ]

admin.site.register(Food, FoodsAdmin)


class ConsumationAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'food',
        'amount_of_food',
        'date',
        'calories_consumated',
    ]

admin.site.register(Consumation, ConsumationAdmin)


class TempAdmin(admin.ModelAdmin):
    list_display = [
        'food1',
        'food1_amount',
        'food2',
        'food2_amount',
    ]

admin.site.register(Temp, TempAdmin)