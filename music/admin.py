from django.contrib import admin

from music.models import Artist, Album, Song, Contact

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["artist_name"]
    search_fields = ["artist_name"]

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["album_title", "album_artist"]
    search_fields = ["album_title", "album_artist"]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["song_title", "song_album"]
    search_fields = ["song_title"]

admin.site.register(Contact)
# Register your models here.
