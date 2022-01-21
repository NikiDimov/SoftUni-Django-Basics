from django.shortcuts import render

from mysite.task.models import Task


def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'index.html', context)
