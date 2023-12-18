from django.urls import path
from apps.todolist import views

app_name = 'todolist'

urlpatterns = [
    path('', views.TodoListView.as_view(), name='todo_list'),
    path('create/', views.TodoCreateView.as_view(), name='todo_create'),
    path('detail/<int:pk>', views.TodoDetailView.as_view(), name='todo_detail'),
    path('update/<int:pk>', views.TodoUpdateView.as_view(), name='todo_update'),
    path('delete/<int:pk>', views.TodoDeleteView.as_view(), name='todo_delete'),
]
