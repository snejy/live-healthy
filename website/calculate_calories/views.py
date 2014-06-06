from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from calculate_calories.forms import LoginForm
from calculate_calories.forms import UserRegistrationForm
from calculate_calories.models import UserProfile
from calculate_calories.forms import UserProfileRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from calculate_calories.helper import calories
from django.contrib.auth import authenticate, login as django_login, logout as django_logout


def home(request):
   return render(request, 'home.html', locals())

def about(request):
   return render(request, 'about.html', locals())


@csrf_protect
def register(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            uform = UserRegistrationForm(data = request.POST)
            pform = UserProfileRegistrationForm(data = request.POST)
            if uform.is_valid() and pform.is_valid():
                balance = calories(pform.cleaned_data['gender'],
                 pform.cleaned_data['kilograms'], 
                 pform.cleaned_data['height'], 
                 pform.cleaned_data['age'], 
                 pform.cleaned_data['sports'])
             
                new_user = User.objects.create_user(
                username=uform.cleaned_data['username'],
                password=uform.cleaned_data['password1'],
                email=uform.cleaned_data['email'],
                first_name = uform.cleaned_data['first_name'],
                last_name = uform.cleaned_data['last_name'])
                user_profile = UserProfile(
                user = new_user,
                gender = pform.cleaned_data['gender'],
                age = pform.cleaned_data['age'],
                kilograms = pform.cleaned_data['kilograms'],
                height = pform.cleaned_data['height'],
                sports = pform.cleaned_data['sports'],
                calorie_balance = balance)
                user_profile.save()
                return HttpResponseRedirect('/home/')
        else:
            uform = UserRegistrationForm(data = request.POST)
            pform = UserProfileRegistrationForm(data = request.POST)
        variables = RequestContext(request, {
        'uform': uform,
        'pform': pform
        })
     
        return render_to_response(
        'register.html',
        variables,
        )
    else:
        return HttpResponseRedirect('/profile/')

# @csrf_protect
def login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    django_login(request, user)
                else:
                    print("The password is valid, but the account has been disabled!")
            else:
                # the authentication system was unable to verify the username and password
                print("The username and password were incorrect.")
            return HttpResponseRedirect('/home/')
    else:
        form = LoginForm(data = request.POST)
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'login.html',
    variables,
    )


@login_required
def track_calories(request):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user = request.user);
    return render(request, 'track_calories.html', locals())


# @login_required
def profile(request):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user = request.user);
    return render(request, 'profile.html', locals())

# @login_required
def logout(request):
    django_logout(request)
    return redirect('/login/')
 