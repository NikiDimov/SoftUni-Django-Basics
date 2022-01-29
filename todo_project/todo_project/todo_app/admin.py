from django.contrib import admin

from todo_project.todo_app.models import Todo


@admin.register(Todo)
class AdminTodo(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'is_done')



