from django import forms
from django.contrib.auth.models import User
from calculate_calories.formfields import ChoiceField
from django.utils.translation import ugettext_lazy as _
from calculate_calories.models import UserProfile
import re
from django import forms
from django.utils.translation import ugettext_lazy as _
 
class UserRegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

    class Meta:
        model = User


class UserProfileRegistrationForm(forms.Form):
    username = forms.CharField(required = True,error_messages={'required': 'Please enter your username'})
    first_name = forms.CharField(required = True,max_length = 30, error_messages={'required': 'Please enter your first name'})
    last_name = forms.CharField(required = True,max_length = 30, error_messages={'required': 'Please enter your last name'})
    gender = forms.ChoiceField(required = True)
    GENDER = (
        ('f', 'female'),
        ('m', 'male')
    )
    gender = forms.CharField(required = True, max_length = 1)
    # date_of_birth = forms.DateField(required = True)    
    kilograms = forms.IntegerField(required = True)
    age = forms.IntegerField(required = True)
    height = forms.IntegerField(required = True)
    SPORTS = (
        (1.2, "Does not do sport."),
        (1.375, "Does sport 1 to 3 times weekly."),
        (1.55, "Does sport 3 to 5 times weekly."),
        (1.725, "Does sport 6 to 7 times weekly."),
        (1.9, "Extreme active: 7 times weekly with additional activities.")
    )
    sports = forms.FloatField(required = True)

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
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))


    # class Meta:
    #     model = User
    #     fields = ('username', 'password')
# class UserForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password',
#                                 widget=forms.PasswordInput())
#     password2 = forms.CharField(label='Password confirmation',
#                                 widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('email', 'password')

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         user = super(UserForm, self).save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


    # class Meta:
    #     model = UserProfile
    #     fields = ['username', 'first_name', 'last_name', 'gender', 
    #     'date_of_birth', 'kilograms', 'height', 'sports']

    # def save(self, profile_callback=None):
    #     new_user = RegistrationProfile.objects.create_inactive_user(username=self.cleaned_data['username'],
    #     password=self.cleaned_data['password1'],
    #     email=self.cleaned_data['email'])
    #     new_profile = UserProfile(user=new_user, city=self.cleaned_data['gender '])
    #     new_profile.save()
    #     return new_user

# form = LoginForm()
# form = RegistrationForm()
# form = UserRegistrationForm()