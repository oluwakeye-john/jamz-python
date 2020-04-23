from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('song/<int:pk>/', views.song_detail, name="song_detail"),
    path('album/<int:pk>/', views.album_detail, name="album_detail"),
    path('album/<int:pk>/<str:state>/', views.album_like_dislike, name="album_like_dislike"),
    path('artist/<int:pk>/', views.artist_detail, name="artist_detail"),
    path('contact/', views.contact, name="contact")
]
