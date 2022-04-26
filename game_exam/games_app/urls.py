from django.urls import path

from game_exam.games_app.views import home, dashboard, game_create, game_details, game_edit, game_delete, \
    profile_details, profile_create, profile_edit, profile_delete

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('game/create/', game_create, name='game_create'),
    path('game/details/<int:pk>/', game_details, name='game_details'),
    path('game/edit/<int:pk>/', game_edit, name='game_edit'),
    path('game/delete/<int:pk>/', game_delete, name='game_delete'),
    path('profile/create/', profile_create, name='profile_create'),
    path('profile/details/', profile_details, name='profile_details'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    path('profile/delete/', profile_delete, name='profile_delete'),
]