from django.db import models
from user1.models import User1
from quiz.models import Quiz
# Create your models here.
class Result(models.Model):
    user = models.ForeignKey(User1, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    time = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user