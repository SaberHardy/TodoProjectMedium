from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import TodoModel


class ViewTodo(ListView):
    model = TodoModel
    template_name = 'todoApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = TodoModel.objects.all()
        return context


# def index(request):
#     todos = TodoModel.objects.all()
#     context = {
#         'todos': todos
#     }
#     return render(request, 'todoApp/index.html', context)



def detail_todo(request, id):
    todo = TodoModel.objects.get(id=id)
    context = {
        'todo': todo
    }
    return render(request, 'todoApp/detail.html', context)


def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')
        completed = 'completed' in request.POST

        # Create and save the new todo item
        todo = TodoModel(title=title, description=description, priority=priority, completed=completed)
        todo.save()

        # Redirect to the main todo list page after saving
        return redirect('index')

    # If not a POST request, render the create todo modal template
    return render(request, 'todoApp/create_todo.html')


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
