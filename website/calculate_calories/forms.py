import re

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from .models import UserProfile, Food, Consumation, Temp
from .formfields import ChoiceField


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label=_('Username'), max_length=50)
    email = forms.EmailField(label=_("Email address"))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(
        required=True,
        max_length=30,
        render_value=False)),
        label=_("Password"))
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(
        required=True,
        max_length=30,
        render_value=False)),
        label=_("Password (again)")
        )
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password != password_confirm:
            raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

    class Meta:
        model = User


class UserProfileRegistrationForm(forms.Form):
    GENDER = (
        ('f', 'female'),
        ('m', 'male')
    )
    SPORTS = (
        (1.2, "Does not do sport."),
        (1.375, "Does sport 1 to 3 times weekly."),
        (1.55, "Does sport 3 to 5 times weekly."),
        (1.725, "Does sport 6 to 7 times weekly."),
        (1.9, "Extreme active: 7 times weekly with additional activities.")
    )
    gender = forms.ChoiceField(required=True, choices=GENDER)
    kilograms = forms.IntegerField(required=True)
    age = forms.IntegerField(required=True)
    height = forms.IntegerField(required=True)
    sports = forms.FloatField(required=True)

    def save(self, *args, **kw):
        super(UserProfileRegistrationForm, self).save(*args, **kw)
        self.instance.user.first_name = self.cleaned_data.get('first_name')
        self.instance.user.last_name = self.cleaned_data.get('last_name')
        self.instance.user.gender = self.cleaned_data.get('gender')
        self.instance.user.kilograms = self.cleaned_data.get('kilograms')
        self.instance.user.height = self.cleaned_data.get('height')
        self.instance.user.sports = self.cleaned_data.get('sports')
        self.instance.user.age = self.cleaned_data.get('age')
        self.instance.user.save()

    class Meta:
        model = UserProfile


class LoginForm(forms.Form):
    username = forms.RegexField(
        regex=r'^\w+$',
        label=_("Username"),
        widget=forms.TextInput(
            attrs=dict(required=True, max_length=30,)
            ),
        error_messages={'invalid':
                      _("This value must contain only letters, numbers and underscores.")}
        )
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(
                               required=True,
                               max_length=30,
                               render_value=False)),
                               label=_("Password"))


class CaloriesForm(forms.Form):
    food_name = forms.ModelMultipleChoiceField(queryset=Food.objects.all())
    amount_of_food = forms.IntegerField(required=True)


class WhatToEatForm(forms.Form):
    food = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        )
    amount = forms.IntegerField(required=True)
    another_food = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        )
    another_amount = forms.IntegerField(required=True)

    class Meta:
        model = Temp
