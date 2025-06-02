from django.shortcuts import render, get_object_or_404
from .models import VideoGame

def home(request):
    return render(request, 'home.html')

def game_list(request):
    games = VideoGame.objects.all().order_by('id')
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(VideoGame, pk=game_id)
    return render(request, 'game_detail.html', {'game': game})
