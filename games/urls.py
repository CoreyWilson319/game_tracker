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
    path('<int:game_id>/', views.game_details, name='game_details'),
    path('<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('user/<username>/', views.profile, name="profile"),
]