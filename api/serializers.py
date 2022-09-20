from rest_framework.serializers import ModelSerializer
from .models import Project,User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ProjectSerializer(ModelSerializer):
    class Meta: 
        model = Project
        fields = ['image', 'name', 'category']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token