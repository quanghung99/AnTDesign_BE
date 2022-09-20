from rest_framework.serializers import ModelSerializer
from .models import Project,User

class ProjectSerializer(ModelSerializer):
    class Meta: 
        model = Project
        fields = ['image', 'name', 'category']

class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        field = ['username', 'password']