from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addgame/', views.add_game, name='add_games')
]