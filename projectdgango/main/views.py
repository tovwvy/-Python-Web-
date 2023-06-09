from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, "main/index.html", {'title': 'Головна сторінка сайту', 'tasks': tasks})


def about(request):
    return render(request, "main/about.html")


def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма не вірна'


    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, "main/create.html", context)

