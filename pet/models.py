from django.db import models
from django.utils import timezone



class ToDoItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)
    check_execute = models.BooleanField(default=False)
    start_date = models.DateField(default=timezone.now)


    def __str__(self):
        return f"{self.text}: start {self.start_date}: due {self.due_date}: {self.check_execute}"

