from django.db import models


class Todo(models.Model):
    todo = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.todo
