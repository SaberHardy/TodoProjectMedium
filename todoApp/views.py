from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import TodoForm
from .models import TodoModel


class ViewTodo(ListView):
    model = TodoModel
    template_name = 'todoApp/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = TodoModel.objects.all()
        return context


class DetailTodo(DetailView):
    model = TodoModel
    template_name = 'todoApp/detail.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super(DetailTodo, self).get_context_data(*args, **kwargs)
        context['todo'] = TodoModel.objects.get(id=self.kwargs['pk'])
        return context


class CreateTodo(CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todoApp/create_todo.html'


class UpdateTodo(UpdateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todoApp/update_todo.html'


def delete_todo(request, id):
    todo = get_object_or_404(TodoModel, id=id)
    todo.delete()
    return redirect('index')
