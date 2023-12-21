from datetime import date
from django.shortcuts import render, redirect, reverse

from django.views.generic import ListView
from .models import ToDoItem



class AllToDos(ListView):
    model = ToDoItem
    template_name = "pet/index.html"

    # def get_queryset(self):
    #     return ToDoItem.objects.filter(due_date__gte=date.today())


class TodayToDos(ListView):
    model = ToDoItem
    template_name = "pet/today.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=date.today())

class OverdueToDos(ListView):
    model = ToDoItem
    template_name = "pet/overdue.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date__lte=date.today())


def change_value(request,pk):
    my_model = ToDoItem.objects.get(id=pk)
    if my_model.check_execute:
        my_model.check_execute = False
    else:
        my_model.check_execute = True
    my_model.save()
    return redirect(request.META.get('HTTP_REFERER'))

class ShemaGantt(ListView):
    model = ToDoItem
    template_name = "pet/gantt.html"

def gantt_chart(request):
    tasks = [
        {'id': 1, 'text': 'Task 1', 'start_date': '2021-10-01', 'duration': 5},
        {'id': 2, 'text': 'Task 2', 'start_date': '2021-10-06', 'duration': 3},

    ]


    return render(request, 'pet/gantt.html', {'tasks': tasks})