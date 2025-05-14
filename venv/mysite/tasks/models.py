from django.db import models

# Create your models here.

class Task(models.Model):

    priority_choice = [("L","Low"),("M","Medium"),("H","High")]


    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    priority = models.CharField(max_length = 1, choices=priority_choice, default = "M")
    due_date = models.DateField(blank = True,null = False)
    completed = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return self.title