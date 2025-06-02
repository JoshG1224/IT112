from django.urls import path
from . import views

urlpatterns = [
    # Home page at "/"
    path('', views.home, name='home'),

    # List all games at "/games/"
    path('games/', views.game_list, name='game_list'),

    # Detail for a single game at "/games/<id>/"
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
]
