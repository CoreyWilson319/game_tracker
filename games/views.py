from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import GameForm
from .models import Game
import requests

# Create your views here.

# def get_games(request):
#     response = requests.get('https://www.giantbomb.com/api/games/?api_key=f786b25c1faa69068cb59b919e5d89089c16268d&format=json&field_list=name,deck,guid,image,platforms,site_detail_url,expected_release_day&offset=0')
#     print(response)


#     return HttpResponse(response)
# Games
def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', { 'games': games})


def add_game(request):
    context = {}

    # create object of Form
    
    form = GameForm(request.POST)

    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "add_games.html", context)

# USER

# Add LoginForm to this line...
from django.contrib.auth.forms import AuthenticationForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
...
def login_view(request):
     # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else: # it was a get request so send the emtpy login form
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def profile(request, username):
    user = User.objects.get(username=username)
    games = Game.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'games': games})