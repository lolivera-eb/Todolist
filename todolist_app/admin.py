from django.contrib import admin
from .models import TodoList, Priority

admin.site.register(TodoList)
admin.site.register(Priority)