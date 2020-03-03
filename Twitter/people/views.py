from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from rest_framework.decorators import api_view


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() # load the profile instance created by the signal
            user.profile.bio = form.cleaned_data.get('bio')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        
        form = SignUpForm()
    context = {'form': form}
    return render(request, 'people/signup.html', context)
    pass


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            print("here baba! here! \n\n")
            # user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('home')
    else:
        # print("babaababababababababababab\n\n\n")
        form = AuthenticationForm()
    return render(request, 'people/login.html', {'form': form})
    pass


def logout(request):
    auth_logout(request)
    return redirect('home')


def home(request):
    user = request.user
    print(user.username)
    return render(request, 'people/home.html', {'user': user})

