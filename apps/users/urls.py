from django.urls import path

from apps.users.views import (
    UserListCreateAPIView, UserAuthAPIView, UserDetailDestroyAPIView
)

urlpatterns = [
    path('auth-token', UserAuthAPIView.as_view(), name='auth_token'),
    path('', UserListCreateAPIView.as_view(), name='users_list'),
    path('<int:id>/', UserDetailDestroyAPIView.as_view(), name='user_detail'),
]

