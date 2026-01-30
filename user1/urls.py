from django.urls import path
from .views import User1ApiVIew

urlpatterns = [
    path('users/', User1ApiVIew.as_view()),
    path('usersx/<int:pk>/', User1ApiVIew.as_view()),
]