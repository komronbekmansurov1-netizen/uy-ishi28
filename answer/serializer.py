from rest_framework.serializers import ModelSerializer
from .models import Answer

class AnswerSerizalizer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Answer