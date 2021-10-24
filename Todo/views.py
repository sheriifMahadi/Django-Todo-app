from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import TaskForm, SearchBar
from .models import Task
from .filter import Search


# Create your views here.
def index(request):
    all_tasks = Task.objects.order_by('date_added')

    # Search bar 
    myFilter = Search(request.GET, queryset=all_tasks)
    all_tasks = myFilter.qs

    # Make a new task
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():

            # Check if Task exists before adding
            task = form.cleaned_data['task']
            if Task.objects.filter(task = task).exists() != True:
                form.save()
            return HttpResponseRedirect(reverse('todo:home'))

    context = {'all_tasks': all_tasks, 
            'form': form,
            'myFilter': myFilter
            }
    return render(request, 'Todo/index.html', context)
    


def editTask(request, pk):
    """Update an existing task"""
    task = Task.objects.get(id=pk)
    
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TaskForm(instance=task)
    else:
        #POST data submitted; process
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo:home'))
    context = {'form': form, 'task': task}
    return render(request, 'Todo/edit.html', context)

def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete() 
    return HttpResponseRedirect(reverse('todo:home'))
       
    context = {'task': task}
    return render(request, 'Todo/index.html', context)

