from django.shortcuts import render 
from rest_framework import viewsets,permissions
from .models import Project
from .serializers import ProjectSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from api import serializers
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    # permissions.IsAuthenticated()
    # def get_permissions(self):
    #     if self.action == 'list':
    #         print(self)
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()]

class GetTokenPair(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except:
            response = {
                'message': 'Account not valid',
        }
            return Response(response, status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)