from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from calculate_calories.forms import WhatToEatForm, LoginForm, CaloriesForm
from calculate_calories.forms import UserRegistrationForm
from calculate_calories.models import Temp, UserProfile, Food, Users_Food
from calculate_calories.forms import UserProfileRegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from calculate_calories.helper import add_food_in_db, get_2_combinations, calories, combine
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from datetime import datetime
from django.db import IntegrityError


def home(request):
   return render(request, 'home.html', locals())


def about(request):
   return render(request, 'about.html', locals())


@csrf_protect
def register(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            uform = UserRegistrationForm(data=request.POST)
            pform = UserProfileRegistrationForm(data=request.POST)
            if uform.is_valid() and pform.is_valid():
                balance = calories(
                 pform.cleaned_data['gender'],
                 pform.cleaned_data['kilograms'],
                 pform.cleaned_data['height'],
                 pform.cleaned_data['age'],
                 pform.cleaned_data['sports'])

                new_user = User.objects.create_user(
                    username=uform.cleaned_data['username'],
                    password=uform.cleaned_data['password1'],
                    email=uform.cleaned_data['email'],
                    first_name=uform.cleaned_data['first_name'],
                    last_name=uform.cleaned_data['last_name'])
                user_profile = UserProfile(
                    user=new_user,
                    gender=pform.cleaned_data['gender'],
                    age=pform.cleaned_data['age'],
                    kilograms=pform.cleaned_data['kilograms'],
                    height=pform.cleaned_data['height'],
                    sports=pform.cleaned_data['sports'],
                    calorie_balance=balance)
                user_profile.save()
                return HttpResponseRedirect('/home/')
        else:
            uform = UserRegistrationForm(data=request.POST)
            pform = UserProfileRegistrationForm(data=request.POST)
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


def track_calories(request):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user=request.user)
        foods = Users_Food.objects.filter(user_id=user_profile)

        combinations = Temp.objects.all()
        if len(combinations) > 0:
            Temp.objects.all().delete()

        cal = user_profile.calorie_balance

        food_today = []
        for food in foods:
            if datetime.today().date() == food.date.date():
                food_today.append(food)
                cal -= food.calories_consumated

    if request.method == 'POST':
        sform = WhatToEatForm(data=request.POST)
        form = CaloriesForm(data=request.POST)
        if form.is_valid():
            food = form.cleaned_data['food_name']
            food_calories = food.first().calories_per_100gr
            calories = form.cleaned_data['amount_of_food'] / 100 * food_calories
            user_food = Users_Food(
            user_id=user_profile,
            food_id=food.first(),
            amount_of_food=form.cleaned_data['amount_of_food'],
            calories_consumated=calories
            )
            user_food.save()
            return HttpResponseRedirect('/track_calories/')

        if sform.is_valid():
            food_to_combine = sform.cleaned_data['food']
            another_food_to_combine = sform.cleaned_data['another_food']
            amount = sform.cleaned_data['amount']
            another_amount = sform.cleaned_data['another_amount']

            for combination in combinations:
                if food_to_combine.first().food_name == combination.food1 and another_food_to_combine.first().food_name == combination.food2:
                    attempt = get_2_combinations(food_to_combine.first().food_type, food_to_combine.first().calories_per_100gr, amount, another_food_to_combine.first().food_type, another_food_to_combine.first().calories_per_100gr, another_amount, cal)
            else:
                attempt = get_2_combinations(food_to_combine.first().food_type, food_to_combine.first().calories_per_100gr, amount, another_food_to_combine.first().food_type, another_food_to_combine.first().calories_per_100gr, another_amount, cal)

            if len(attempt) < 2 and len(attempt) > 0:
                food_try = Temp(
                    food1=food_to_combine.first().food_name,
                    food1_amount=attempt[0][1],
                    )
                food_try.save()
            elif attempt:
                for i in range(0, len(attempt)-1):
                    try:
                        food_try = Temp(
                            food1=food_to_combine.first().food_name,
                            food2=another_food_to_combine.first().food_name,
                            food1_amount=attempt[i][i+1],
                            food2_amount=attempt[i+1][i+1]
                            )
                    except IndexError as e:
                        return HttpResponseRedirect('/track_calories/')

                    try:
                        food_try.save()
                    except IntegrityError as e:
                        return HttpResponseRedirect('/track_calories/')

            return HttpResponseRedirect('/track_calories/')
    else:
        sform = WhatToEatForm()
        form = CaloriesForm()
    variables = RequestContext(request, {
    'form': form,
    'sform': sform,
    })
    return render_to_response("track_calories.html", locals(), variables)


def login(request):
    try:
        add_food_in_db()
    except IntegrityError as e:
        return HttpResponseRedirect('/login/')

    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
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
        form = LoginForm(data=request.POST)
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'login.html',
    variables,
    )


@login_required
def profile(request):
    if request.user.is_authenticated():
        user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'profile.html', locals())


@login_required
def logout(request):
    django_logout(request)
    return redirect('/login/')
