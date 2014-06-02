from django.contrib import admin
from calculate_calories.models import UserProfile

class UsersAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
        'first_name',
        'last_name',
        'gender',
        'sports',
        # 'date_of_birth',
        'calorie_balance',
    ]

admin.site.register(UserProfile, UsersAdmin)