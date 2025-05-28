from django.shortcuts import render
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request,'task/task_list.html',{'task':tasks})
