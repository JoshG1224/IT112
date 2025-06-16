from django.urls import path
from . import views

urlpatterns = [
    # (1) Existing home + games pages might already be here:
    path("", views.home, name="home"),
    path("games/", views.game_list, name="game_list"),
    path("games/<int:game_id>/", views.game_detail, name="game_detail"),

    # (2) New API endpoints:
    path("api/games/all/", views.api_all_games, name="api_all_games"),
    path("api/games/one/", views.api_game_by_id, name="api_game_by_id"),
    path("api/games/create/", views.api_create_game, name="api_create_game"),
]
