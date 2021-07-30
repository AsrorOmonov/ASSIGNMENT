from django.urls import path

from main.views import UserDetailView, UserCreateView, UserUpdateView, UserListView, UserDeleteView

app_name = 'main'

urlpatterns = [
    path('detail/<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/', UserUpdateView.as_view(), name='edit'),
    path('', UserListView.as_view(), name='list'),
]
