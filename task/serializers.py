from rest_framework import serializers
from .models import Task

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = 'title', 'description', 'status'
        
class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'