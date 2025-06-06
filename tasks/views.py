from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from datetime import date
from django.contrib.auth import login 
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    filter_type = request.GET.get('filter')
    
    if request.user.is_authenticated:
        if filter_type == 'pending':
            tasks = Task.objects.filter(user=request.user, status='pending').order_by('due_date')
        elif filter_type == 'today':
            tasks = Task.objects.filter(user=request.user, due_date=date.today()).order_by('due_date')
        else:
            tasks = Task.objects.filter(user=request.user).order_by('due_date')
    else:
        tasks = []
    
    return render(request, 'tasks/home.html', {'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('home')

    else:
        form = TaskForm()
    return render(request,'tasks/add_task.html',{'form':form})


def edit_task(request,task_id):
    task = get_object_or_404(Task,pk = task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance = task)
    return render(request,'tasks/edit_task.html',{'form':form})


def delete_task(request,task_id):

    task = get_object_or_404(Task,pk = task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request,'tasks/delete_task.html',{'task':task})


def toggle_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.status = 'completed' if task.status == 'pending' else 'pending'
    task.save()
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'tasks/signup.html', {'form': form})
