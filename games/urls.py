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
    path('user/<username>/notes', views.notes_view, name='notes'),
    path('<int:game_id>/', views.game_details, name='game_details'),
    path('<int:pk>/update/', views.GameUpdate.as_view(), name='games_update'),
    path('<int:pk>/delete/', views.GameDelete.as_view(), name='games_delete'),
    path('<int:pk>/add/', views.Add_to_favorite, name = 'add_to_favorite'),
    path('user/<username>/', views.profile, name="profile"),
    path('<int:game_id>/<username>/notes/create/', views.NoteCreate.as_view(), name='note_create'),
    path('<int:game_id>/<username>', views.user_game_details, name="user_game_details"),
    # path('<int:pk>/update/', views.NoteUpdate.as_view(), name='notes_update'),
    path('<int:pk>/<username>/note/delete/', views.NoteDelete.as_view(), name='note_delete'),
]