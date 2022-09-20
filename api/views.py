from django.shortcuts import render 
from rest_framework import viewsets,permissions
from .models import Project
from .serializer import ProjectSerializer


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