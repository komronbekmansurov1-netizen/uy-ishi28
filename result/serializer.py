from rest_framework.serializers import ModelSerializer
from .models import Result

class ResultSerizalizer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Result