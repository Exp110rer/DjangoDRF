from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from authors.serializers import AuthorModelSerializer
from authors.models import Authors

# Create your views here.

class AuthorModelViewSet(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorModelSerializer