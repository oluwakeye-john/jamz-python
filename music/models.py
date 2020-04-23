from django.db import models
from users.models import User


class Artist(models.Model):
    artist_name = models.CharField(max_length=255)

    def __str__(self):
        return self.artist_name
    

class Album(models.Model):
    album_title = models.CharField(max_length=255)
    album_cover = models.ImageField(upload_to="album-cover")
    album_artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255, default="")
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    release_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.album_title
    

class Song(models.Model):
    song_title = models.CharField(max_length=255)
    song_album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_file = models.FileField(upload_to="songs-file")
    song_rating = models.IntegerField(default=0)
    def __str__(self):
        return self.song_title


class Contact(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    albums = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

# Create your models here.
