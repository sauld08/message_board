from django.shortcuts import render
from .models import Task
from django.views.generic import ListView
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'tasks_list.html'