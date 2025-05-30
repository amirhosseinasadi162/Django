from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task

from .forms import TaskForm

# Create your views here.

# show tasks
@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request,'task/task_list.html',{'tasks':tasks})

# add task
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request,'task/add_task.html',{'form':form})

#edit task 
@login_required
def edit_task(request,task_id):
    task = get_object_or_404(Task,id = task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance = task)
    return render(request,'task/edit_task.html',{'form':form,'task':task})

#delete task
@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task,id = task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'task/delete_task.html',{'task':task})

#change the completed
@login_required
def toggle_complete(request,task_id):
    task = get_object_or_404(Task,id = task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')