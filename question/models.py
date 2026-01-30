from django.db import models
from quiz.models import Quiz
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    ball = models.IntegerField(default=10)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
