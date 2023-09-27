from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name='user-list'),
    path('courses/', views.get_lesson, name='course-list'),
    
]
