from django.shortcuts import render
from django.http import JsonResponse

def game_board(request):
    return render(request, 'game_board.html')

def home(request):
    return render(request, 'home.html')

