from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name='user-list'),
    path('login/', views.user_login, name='user-login'),
]
