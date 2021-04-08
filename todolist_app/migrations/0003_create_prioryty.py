from django.db import migrations
from todolist_app.models import Priority

def create_priorities(*args):
    Priority.objects.bulk_create([
        Priority(description='Low', order=0),
        Priority(description='Normal', order=1),
        Priority(description='Urgent', order=2),
        Priority(description='Super Urgent', order=3),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_todolist_user'),
    ]

    operations = [
        migrations.RunPython(create_priorities),
    ]
    