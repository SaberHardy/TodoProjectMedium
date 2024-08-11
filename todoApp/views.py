from django.shortcuts import render

from .models import TodoModel


def index(request):
    todos = TodoModel.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todoApp/home.html', context)


def todos(request):
    return render(request, 'todoApp/todos.html')
