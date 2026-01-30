from django.urls import path
from .views import AnswerApiVIew

urlpatterns = [
    path('answer/', AnswerApiVIew.as_view()),
    path('answer/<int:pk>/', AnswerApiVIew.as_view()),
]