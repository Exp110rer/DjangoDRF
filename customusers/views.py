from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from customusers.models import CustomUsers
from customusers.serializers import CustomUsersModelSerializer

# Create your views here.

class CustomUsersModelViewSet(ModelViewSet):
    queryset = CustomUsers.objects.all()
    serializer_class = CustomUsersModelSerializer
