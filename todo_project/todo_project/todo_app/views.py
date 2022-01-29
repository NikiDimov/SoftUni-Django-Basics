
from django.shortcuts import render

from todo_project.todo_app.models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'common.html', context)
