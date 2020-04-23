from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from users import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("music.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', auth_view.register, name="register"),
    path('accounts/profile/', auth_view.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
