from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import posts_list, posts_detail, posts_create, posts_update, posts_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_list),
    path('posts/create/', posts_create),
    path('posts/<int:pk>/', posts_detail),
    path('posts/<int:pk>/update/', posts_update),
    path('posts/<int:pk>/delete/', posts_delete),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


