from rest_framework import fields, serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo 
        fields = ('id','title','description','completed')

        