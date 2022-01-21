from django.urls import path

from mysite.task.views import index

urlpatterns = [
    path('', index, name='index')
]
