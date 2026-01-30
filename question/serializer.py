from rest_framework.serializers import ModelSerializer
from .models import Question

class QuestionSerizalizer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Question