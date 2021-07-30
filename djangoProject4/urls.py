
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from djangoProject4 import settings
# from main.views import UserListView, UserUpdateView, UserCreateView, UserDetailView, UserDeleteView

urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
    path('', include('main_page.urls', 'main'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
