from django.shortcuts import render, redirect
from .models import Task

def addTask(request):
    if request.method == 'POST':
        task = request.POST['task']
        Task.objects.create(task=task)
        return redirect('/')

    return redirect('/')