from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoGame


def home(request):
    """
    Simple homepage view—either render a template or just return plain text.
    If you already have a 'home.html' from HW8, use this:
    """
    return render(request, 'home.html')

def game_list(request):
    games = VideoGame.objects.all().order_by('id')
    return render(request, 'game_list.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(VideoGame, pk=game_id)
    return render(request, 'game_detail.html', {'game': game})

def api_all_games(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET allowed here."}, status=200)
    games_qs = VideoGame.objects.all().values("id", "title", "genre", "platform")
    return JsonResponse(list(games_qs), safe=False, status=200)

def api_game_by_id(request):
    if request.method != "GET":
        return JsonResponse({"error": "Only GET allowed here."}, status=200)
    game_id = request.GET.get("id")
    if not game_id:
        return JsonResponse({"error": "Missing 'id' query parameter."}, status=200)
    try:
        game = VideoGame.objects.get(pk=int(game_id))
    except (VideoGame.DoesNotExist, ValueError):
        return JsonResponse({"error": f"VideoGame with id={game_id} not found."}, status=200)
    data = {"id": game.id, "title": game.title, "genre": game.genre, "platform": game.platform}
    return JsonResponse(data, status=200)

@csrf_exempt
def api_create_game(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed here."}, status=200)
    try:
        payload = json.loads(request.body.decode("utf-8"))
        title = payload["title"]
        genre = payload["genre"]
        platform = payload["platform"]
    except (json.JSONDecodeError, KeyError):
        return JsonResponse(
            {"error": "Invalid JSON body or missing fields (title, genre, platform)."}, status=200
        )
    try:
        new_game = VideoGame.objects.create(title=title, genre=genre, platform=platform)
    except Exception as e:
        return JsonResponse({"error": f"Failed to insert: {str(e)}"}, status=200)
    return JsonResponse({"message": "Game created", "id": new_game.id}, status=200)
