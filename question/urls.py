from django.urls import path
from .views import QuestionApiVIew

urlpatterns = [
    path('question/', QuestionApiVIew.as_view()),
    path('question/<int:pk>/', QuestionApiVIew.as_view()),
]