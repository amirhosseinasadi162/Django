from django.db import models

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES = [
        ('L','LOW'),
        ('M','Medium'),
        ('H','High'),
    ]

    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    completed = models.BooleanField(default = False)
    due_date = models.DateField(null = True,blank = True)
    priority = models.CharField(max_length = 1, choices = PRIORITY_CHOICES,default = 'M')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title