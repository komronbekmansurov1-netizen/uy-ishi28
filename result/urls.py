from django.urls import path
from .views import ResultApiVIew

urlpatterns = [
    path('result/', ResultApiVIew.as_view()),
    path('result/<int:pk>/', ResultApiVIew.as_view()),
]