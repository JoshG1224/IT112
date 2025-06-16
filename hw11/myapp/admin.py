from django.contrib import admin
from .models import VideoGame

@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'title', 'genre', 'platform')
    
    search_fields = ('title', 'genre', 'platform')
    
    list_filter = ('genre', 'platform')
