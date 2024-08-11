from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import TodoModel


def index(request):
    todos = TodoModel.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todoApp/index.html', context)


def detail_todo(request, id):
    todo = TodoModel.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todoApp/detail.html', context)


def create_todo(request):
    return render(request, 'todoApp/create.html')


def update_todo(request, id):
    todo = get_object_or_404(TodoModel, pk=id)

    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.priority = request.POST.get('priority')
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('index')

    return render(request, 'todoApp/update_todo.html', {'todo': todo})


def delete_todo(request, id):
    todo = get_object_or_404(TodoModel, id=id)
    todo.delete()
    return redirect('index')
