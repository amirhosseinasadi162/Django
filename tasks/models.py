from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):

    PRIORITY_CHOICES = [
        ('low', 'کم'),
        ('medium', 'متوسط'),
        ('high', 'زیاد'),
    ]

    STATUS_CHOICES = [
        ('pending', 'در انتظار'),
        ('completed', 'انجام شده'),
    ]

    title = models.CharField(max_length = 255)
    description = models.TextField(blank = True)
    due_date = models.DateField()
    priority = models.CharField(max_length = 10, choices = PRIORITY_CHOICES,default = 'medium')
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES,default = 'pending')
    created_at = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)


    def __str__(self):
        return self.title