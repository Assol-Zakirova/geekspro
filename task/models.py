from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    title = models.TextField()
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')
    tags = models.ManyToManyField(Tag, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

