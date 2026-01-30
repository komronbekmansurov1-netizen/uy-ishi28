from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User1(AbstractUser):
    age = models.IntegerField(default=0)
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
