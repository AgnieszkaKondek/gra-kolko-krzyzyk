from django.urls import path
from .views import game_board
from .views import home

urlpatterns = [
    path('', home, name='home'), 
    path('game-board/', game_board, name='game_board'),
]



