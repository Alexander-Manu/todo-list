import re
from django.shortcuts import render, redirect
from django.db.models import Q
from base.forms import AddTaskForm, UpdateTaskForm, RegisterUserForm
from .models import Task, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist!')
    return render(request, 'base/login.html')



def logoutUser(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            new_user = authenticate(username=username, password=password)
            if new_user is not None:
                login(request, new_user)
                return redirect('home')
        else:
            messages.error(request, 'Oops! An error occured during registration, Please try again!!!')  
    form = RegisterUserForm()
    return render(request, 'base/register.html', {'form':form})


@login_required(login_url='login')
def home(request):
    search_task = request.GET.get('q')
    if search_task:
        tasks = Task.objects.filter(Q(title__icontains=search_task))
    else:
    # If not searched, return default posts
        tasks = Task.objects.all()

    # tasks = Task.objects.all()
    tasks_count = Task.objects.filter(completed=False, user = request.user)
    count_incomplete_task = tasks_count.count()

    context = {'tasks':tasks, 'count_incomplete_task':count_incomplete_task}
    return render(request, 'base/home.html', context)


@login_required(login_url='login')
def createTask(request):
    form = AddTaskForm()
    if request.method == 'POST':
        Task.objects.create(user = request.user, title = request.POST.get('title'), description = request.POST.get('description'))
        return redirect('home')
    return render(request, 'base/addTask_form.html', {'form':form})


@login_required(login_url='login')
def updateTask(request, pk):
    tasks = Task.objects.get(id=pk)
    form = UpdateTaskForm(instance = tasks)
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        return render(request, 'base/updateTask_form.html',{'tasks':tasks, 'form':form})



@login_required(login_url='login')
def deleteTask(request, pk):
    tasks = Task.objects.get(id=pk)
    if request.method == 'POST':
        tasks.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':tasks})


@login_required(login_url='login')
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    context= {'task':task}
    return render(request, 'base/task_Detail.html', context)