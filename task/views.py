from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request,'task/task_list.html',{'task':tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request,'task/add_task.html',{'form':form})
    