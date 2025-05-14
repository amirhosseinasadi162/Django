from django.shortcuts import render
from .models import Task
# Create your views here.

def task_list(requset):

    tasks = Task.objects.all().order_by("-created_at")
    return render(requset,'tasks/task_list.html',{'tasks':tasks})