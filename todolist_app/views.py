from django.shortcuts import render
from .models import TodoList
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.
class TodoListCreate(generic.CreateView):
    model = TodoList
    fields = ["descripcion","done","priority"]
    success_message = "created"
    success_url = reverse_lazy('todolist_app:todolist_view')
    def form_valid (self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoListView(generic.ListView):
    model = TodoList
    context_object_name = "obj"
    fields = '__all__'
    success_url = reverse_lazy('todolist_app:todolist_view')

class TodoEdit(generic.UpdateView):
    model = TodoList
    fields = '__all__'
    context_object_name = "obj"
    success_url = reverse_lazy('todolist_app:todolist_view')
    success_message = "todo update"

class TodoDel(generic.DeleteView):
    model = TodoList
    context_object_name = "obj"
    success_url = reverse_lazy('todolist_app:todolist_view')


class UserEdit(generic.UpdateView):
    model = TodoList
    fields = ['user']
    success_url = reverse_lazy('todolist_app:todolist_view')