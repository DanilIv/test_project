from django.urls import path
from . import views
from .views import change_value

urlpatterns = [
    path("", views.AllToDos.as_view(), name="index"),
    path("today/", views.TodayToDos.as_view(), name="today"),
    path("overdue/", views.OverdueToDos.as_view(), name="overdue"),
    path('change_value/<int:pk>/', change_value, name='change_value'),
    path("gantt", views.ShemaGantt.as_view(), name="gantt"),
]