from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('addgame/', views.add_game, name='add_game'),
    path('', views.index, name='games'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('user/<username>/', views.profile, name='profile'),
]