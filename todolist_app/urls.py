from django.contrib import admin
from django.urls import path
from .views import TodoListCreate, TodoListView, TodoEdit, TodoDel, UserEdit

urlpatterns = [
   path('create/', TodoListCreate.as_view() , name='todo_form'),
   path('', TodoListView.as_view() , name='todolist_view'),
   path('update/<int:pk>', TodoEdit.as_view() , name='todo_update'),
   path('delete/<int:pk>', TodoDel.as_view() , name='todo_delete'),
   path('updateUser/<int:pk>', UserEdit.as_view() , name='user_update'),
]
