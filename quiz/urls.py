from django.urls import path
from .views import QuizApiVIew

urlpatterns = [
    path('quiz/', QuizApiVIew.as_view()),
    path('quiz/<int:pk>/', QuizApiVIew.as_view()),
]