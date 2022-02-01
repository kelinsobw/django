from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from blog.views import register
from home.views import home_index
from posts.views import post_list, post_add
from profiles.views import profiles_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name="home"),
    path('posts/add/', post_add, name="post_add"),
    path('profiles/', profiles_index, name="profiles_index"),
    path('register/', register, name="register"),
    path("api/", include("api.urls", namespace="api")),
    path('home/', home_index)
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
