from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"todo № {self.id}"
