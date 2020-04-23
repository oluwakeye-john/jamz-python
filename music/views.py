from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Album, Artist, Song
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required

from .forms import NewContactForm
from django.middleware.csrf import get_token
from .models import Contact

def home(request):
    if request.is_ajax():
        print("AJAX")
        query = request.GET.get("q")
        print(query)
        if len(query) >= 3:
            albums = Album.objects.filter(album_title__icontains = query)[0:5]
            songs = Song.objects.filter(song_title__icontains = query)[0:5]
            artists = Artist.objects.filter(artist_name__icontains = query)[0:5]

            html = render_to_string(   
                template_name="music/ajax_search.html", 
                context={"albums": albums, "songs": songs, "artists":artists}
            )
            return HttpResponse(html)
            
        else:
            return HttpResponse("")

    elif request.method == "GET":
        query = request.GET.get("search")
        if query:
            albums = Album.objects.filter(album_title__icontains = query)
            songs = Song.objects.filter(song_title__icontains = query)
            artists = Artist.objects.filter(artist_name__icontains = query)
            search_number = len(albums) + len(songs) + len(artists)
            main_msg = "Search result for {}({})".format(query, search_number)
            
            msg_albums = "Albums"
            msg_songs = "Songs"
            msg_artists = "Artists"
        else:
            albums = Album.objects.all().order_by("-likes")
            songs = []
            artists = []
            main_msg = ""
            
            msg_albums = "Top Albums"
            msg_songs = "Top Artists"
            msg_artists = "Top Artists"
        
        contact_f = NewContactForm()
        contact_form = render_to_string(template_name="music/contact.html", context={
            "form": contact_f,
            "csrfmiddlewaretoken": get_token(request)
        })
        
        return render(request, template_name="music/home.html", context={
            "albums": albums,
            "songs": songs,
            "artists": artists,
            "main_msg": main_msg,
            "msg_albums": msg_albums,
            "msg_songs": msg_songs,
            "msg_artists": msg_artists,
            "contact_form": contact_form

        })

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    songs = Song.objects.filter(song_album = album)
    more_albums = Album.objects.filter(album_artist = album.album_artist)

    like_dislike = render_to_string(template_name="music/like_dislike.html", context={
        "album_likes": album.likes,
        "album_dislikes": album.dislikes
    })

    return render(request, template_name="music/album_detail.html", context={
        "album": album,
        "songs": songs,
        "more_albums": more_albums,
        "like_dislike": like_dislike
    })

def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    album = song.song_album
    return render(request, template_name="music/song_detail.html", context={
        "song": song,
        "album": album
    })

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    albums = Album.objects.filter(album_artist=artist)
    return render(request, template_name="music/artist_detail.html", context={
        "artist": artist,
        "albums": albums
    })


def album_like_dislike(request, pk, state):
    if request.is_ajax():
        print("AJAX like")
        album = get_object_or_404(Album, pk=pk)
        print(album)
        if request.user.is_authenticated:
            if state == "like":
                album.likes += 1
                list_dislike_msg = "Liked"
            elif state == "dislike":
                album.dislikes += 1
                list_dislike_msg = "Disliked"

            album.save()
            print(album.likes, album.dislikes)
            html = render_to_string(template_name="music/like_dislike.html", context={
                "album_likes": album.likes,
                "album_dislikes": album.dislikes,
                "list_dislike_msg": list_dislike_msg,
                "msg_color": "green"
            })
            print("Django done")
            return HttpResponse(html)
        else:
            list_dislike_msg = "Login required"
            html = render_to_string(template_name="music/like_dislike.html", context={
                "album_likes": album.likes,
                "album_dislikes": album.dislikes,
                "list_dislike_msg": list_dislike_msg,
                "msg_color": "red"
            })
            print("Django done")
            return HttpResponse(html)
    else:
        pass


def contact(request):
    if request.is_ajax():
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact_form = Contact(name=name, email=email, message=message)
        contact_form.save()
        print(name)
        return HttpResponse("Success")