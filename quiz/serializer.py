from rest_framework.serializers import ModelSerializer
from .models import Quiz

class QuizSerizalizer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Quiz