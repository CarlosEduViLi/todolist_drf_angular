from typing import Any
from django import template
from django.db.models.query import QuerySet
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from apps.todolist.models import Todo
from apps.todolist.forms import TodoForm
from apps.todolist.filters import TodoFilter

register = template.Library()

class MyPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                return self.num_pages
            elif int(number) < 1:
                return 1
            else:
                raise

class TodoListView(ListView):
    model = Todo
    queryset = Todo.objects.all()
    template_name = 'apps/todolist/todo_list.html'
    context_object_name = 'todos'
    todo_filter = TodoFilter()
    paginate_by = 8  # Define a quantidade de itens por página
    paginator_class = MyPaginator
    
    @register.simple_tag(takes_context=True)
    def param_replace(context, **kwargs):
        d = context['request'].GET.copy()
        for k, v in kwargs.items():
            d[k] = v
        for k in [k for k, v in d.items() if not v]:
            del d[k]
        return d.urlencode()
    
    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset=super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = TodoFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        page = self.request.GET.get('page', 1)
        todos = self.get_queryset()
        paginator = self.paginator_class(todos, self.paginate_by)
        todos = paginator.page(page)
        context['todos'] = todos
        return context
    
    
    
    # #Função para guardar as informações de cada página, listando os itens
    # def dispatch(self, request, *args, **kwargs):
    #     qs = super().get_queryset()
    #     self.paginate_by = qs.count() if qs.count() < Todo.objects.all().count() else 10
    #     return super().dispatch(request,*args,**kwargs)
    
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