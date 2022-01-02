from django.shortcuts import render
from rest_framework import serializers, viewsets
from .serializers import ToDoSerializer
from .models import ToDo
# Create your views here.


class ToDOView(viewsets.ModelViewSet):
    serializer_class= ToDoSerializer
    queryset= ToDo.objects.all()