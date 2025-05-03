from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Board_Column(models.Model):
    name = models.CharField(max_length=50)
    position = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [
       ('low', 'Low'),
       ('medium', 'Medium'),
       ('high', 'High'),
    ]

    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey(Board_Column, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title