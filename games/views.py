from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import GameForm
from .models import Game, Note
import requests

# Create your views here.

# def get_games(request):
#     response = requests.get('https://www.giantbomb.com/api/games/?api_key=f786b25c1faa69068cb59b919e5d89089c16268d&format=json&field_list=name,deck,guid,image,platforms,site_detail_url,expected_release_day&offset=0')
#     print(response)


#     return HttpResponse(response)
# Games
def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})


def game_details(request, game_id):
    game = Game.objects.get(id=game_id)

    return render(request, 'games/show.html', {'game': game})


def add_to_playing(request, pk):
    if request.user.is_authenticated:
        current_user = request.user
        game = Game.objects.get(id=pk)
        game.users.add(str(current_user.id))
        game.save()

    username = request.user.username

    return render(request, 'profile.html', {'game': game, 'username':username})
    
# COME BACK TO THIS
# def remove_from_playing(request, pk, username):
#     if request.user.is_authenticated:
#         current_user = request.user
#         game = Game.objects.get(id=pk)
#         game.users.filter(current_user.id)
#         print('FILTERED game user', game.users.filter(current_user.id))
#         print(game)
#         # game.users.add(str(current_user.id))
#         game.save()

#     username = request.user.username

#     return render(request, 'profile.html', {'game': game, 'username':username})

def add_game(request):
    context = {}

    # create object of Form

    form = GameForm(request.POST)

    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "add_games.html", context)


class GameUpdate(UpdateView):
    model = Game
    fields = ['title', 'platforms', 'description']

    def form_valid(self, form):
        print(self)
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/games')


class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

# USER


# Add LoginForm to this line...
# ...and add the following line...
...


def login_view(request):
    # if post, then authenticate (user submitted username and password)
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/games/user/'+u)
                else:
                    print('The account has been disabled.')
            else:
                print('The username and/or password is incorrect.')
    else:  # it was a get request so send the emtpy login form
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
            print(user)
            login(request, user)
            return HttpResponseRedirect('/games/user/' + str(user))
        else:
            print('not valid..........................................')
            form = UserCreationForm()
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def profile(request, username):
    user = User.objects.get(username=username)
    games = Game.objects.filter(users=user.id)
    return render(request, 'profile.html', {'username': username, 'games': games, 'user': user})


def user_game_details(request, username, game_id):
    user = User.objects.get(username=username)
    game = Game.objects.get(id=game_id)
    notes = Note.objects.filter(game_id = game_id, user = user.id)

    return render(request, 'user_games.html', {'username': username, 'game': game, 'user': user, 'notes':notes})
## Notes ##


class NoteCreate(CreateView):
    model = Note
    fields = ['content']
    success_url = '/games'

    def form_valid(self, form):
        test = str(self.request)
        the_game_id = int(test.split('/')[2])
        form.instance.user = self.request.user
        form.instance.game_id = the_game_id
        form.save()


        return super(NoteCreate, self).form_valid(form)

def notes_view(request, username):
    print(request.user.id)
    notes = Note.objects.filter(user_id = request.user.id)
    
    return render(request, 'user_notes.html', {'notes': notes})

# class NoteUpdate(UpdateView):
#     model = Note
#     fields = ['content']

#     def form_valid(self, form):
#         print(self)
#         self.object = form.save(commit=False)
#         self.object.save()
#         return HttpResponseRedirect('/games')


class NoteDelete(DeleteView):
    model = Note
    success_url = '/games'


# Need to create delete route for notes