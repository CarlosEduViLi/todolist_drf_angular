from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from apps.todolist.models import Todo
from apps.todolist.forms import TodoForm

class TodoListView(ListView):
    model = Todo
    template_name = 'apps/todolist/todo_list.html'
    context_object_name = 'todos'
    paginate_by = 8  # Define a quantidade de itens por página

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