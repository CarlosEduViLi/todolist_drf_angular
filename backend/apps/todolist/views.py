from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from apps.todolist.models import Todo
from apps.todolist.forms import TodoForm
from apps.todolist.filters import TodoFilter

class TodoListView(ListView):
    model = Todo
    queryset = Todo.objects.all()
    template_name = 'apps/todolist/todo_list.html'
    context_object_name = 'todos'
    todo_filter = TodoFilter()
    paginate_by = 8  # Define a quantidade de itens por página
    
    def get_queryset(self):
        queryset=super().get_queryset()
        self.filterset = TodoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

class TodoCreateView(CreateView):
    model = Todo
    template_name = 'apps/todolist/todo_create.html'
    form_class = TodoForm
    success_url = reverse_lazy('todolist:todo_list')

class TodoDetailView(DetailView):
    model = Todo
    template_name = 'apps/todolist/todo_detail.html'
    
class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'apps/todolist/todo_update.html'
    form_class = TodoForm
    success_url = reverse_lazy('todolist:todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'apps/todolist/todo_confirm_delete.html'  # Novo template sobrescrito
    success_url = reverse_lazy('todolist:todo_list')