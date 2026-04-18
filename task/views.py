from django.shortcuts import render
from rest_framework.response import Response
from task.models import Category, Tag
from .serializers import TaskListSerializer, TaskDetailSerializer
from .models import Task
from rest_framework import generics, status
from django.db import transaction

# Create your views here.

class TaskListApiView(generics.ListCreateAPIView):  
    queryset = Task.objects.all() 
    serializer_class = TaskListSerializer
    def perform_create(self, serializer):
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            task_status = self.request.data.get('task_status')
            category_name = self.request.data.get('category_name', '')
            category, _ = Category.objects.get_or_create(name=category_name)
            tags_names = self.request.data.get('tags_names', "")
            tag, _ = Tag.objects.get_or_create(name=tags_names)
            with transaction.atomic():       
                task = Task.objects.create(
                    title=title,
                    description=description,
                    status=task_status,
                    category=category,
                    )
                task.tags.set([tag])
                task.save()
            return Response(status=status.HTTP_201_CREATED,
                    data=TaskListSerializer(task).data)
    
class TaskDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'
    def perform_update(self, serializer):
        category = self.request.data.get('category')
        category, _ = Category.objects.get_or_create(name=category)

        tags = self.request.data.get('tags')
        tags, _ = Tag.objects.get_or_create(name=tags)

        task = serializer.save(category=category)

        task.tags.set([tags])