from django.db import models
from django.conf import settings
# Create your models here.
class Priority(models.Model):
    description = models.CharField(max_length=100, help_text='Description priority', unique=True)
    order = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.description)

class TodoList(models.Model):
    descripcion = models.CharField(max_length=100, help_text='Description todo', unique=True)
    done = models.BooleanField(default=True)
    priority = models.ForeignKey(Priority ,on_delete = models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
        null=True,
    )
    def __str__(self):
        return '{}'.format(self.descripcion)
