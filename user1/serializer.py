from rest_framework.serializers import ModelSerializer
from .models import User1

class User1Serizalizer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User1

