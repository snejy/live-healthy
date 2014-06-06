from django.contrib import admin
from calculate_calories.models import UserProfile

class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'gender',
        'sports',
        'calorie_balance',
    ]

admin.site.register(UserProfile, UsersAdmin)