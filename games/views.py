from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import GameForm
import requests

# Create your views here.
def index(request):
    return HttpResponse("hello world")

# def get_games(request):
#     response = requests.get('https://www.giantbomb.com/api/games/?api_key=f786b25c1faa69068cb59b919e5d89089c16268d&format=json&field_list=name,deck,guid,image,platforms,site_detail_url,expected_release_day&offset=0')
#     print(response)


#     return HttpResponse(response)

def add_game(request):
    context = {}

    # create object of Form
    
    form = GameForm(request.POST)

    if form.is_valid():
        form.save()

    context['form']= form
    return render(request, "add_games.html", context)
