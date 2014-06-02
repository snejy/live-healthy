from django.shortcuts import render
from django.http import HttpResponseRedirect
from calculate_calories.forms import LoginForm
from calculate_calories.forms import UserRegistrationForm
from calculate_calories.models import UserProfile
from calculate_calories.forms import UserProfileRegistrationForm
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from calculate_calories.helper import calories

def home(request):
   return render(request, 'home.html', locals())

 
@csrf_protect
def register(request):
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
            email=uform.cleaned_data['email'])
            user_profile = UserProfile(
            user = new_user,
            username = uform.cleaned_data['username'],
            first_name = pform.cleaned_data['first_name'],
            last_name = pform.cleaned_data['last_name'],
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

# @csrf_protect
def login(request):
    if request.method == 'POST':
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            return HttpResponseRedirect('/home/')
    else:
        form = LoginForm(data = request.POST)
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'home.html',
    variables,
    )
# return render(request, 'base.html', locals())    
