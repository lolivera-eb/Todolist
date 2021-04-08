from django.test import TestCase
from todolist_app.models import Priority, TodoList
from parameterized import parameterized

class PriorityTest(TestCase):
    @parameterized.expand([
        ["low", 1],
        ["medium", 2],
        ["hard", 3],
    ])
    def test_priority(self,description_p , order_p):
        priority = Priority.objects.create(description = description_p, order = order_p)
        label_description = priority._meta.get_field('description').verbose_name
        label_order = priority._meta.get_field('order').verbose_name
        self.assertEqual(label_description, 'description' )
        self.assertEqual(label_order, 'order' )

class TodoListTest(TestCase):
    @parameterized.expand([
        ["low", 1, 'dormir', True],
        ["medium", 2, 'correr', False],
        ["hard", 3, 'leer', True],
    ])   
    def test_todolist(self,d_priority, o_priority, d_todo, done_todo):
        priority = Priority.objects.create(description = d_priority, order = o_priority) 
        todo = TodoList.objects.create(descripcion =  d_todo, done = done_todo, priority = priority )
        label_description = todo._meta.get_field('descripcion').verbose_name
        label_priority = todo._meta.get_field('priority').verbose_name
        label_done = todo._meta.get_field('done').verbose_name
        self.assertEqual(label_description, 'descripcion' )
        self.assertEqual(label_priority, 'priority' )
        self.assertEqual(label_done, 'done' )