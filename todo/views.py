from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import TodoList
from .forms import TodoForm
# Create your views here.
def create_view(request):
    template_name = 'create.html'
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo:todo_view'))
    else:
        form = TodoForm()
    return render(request, template_name, {'form':form})


def todo_view(request):
    template_name = 'index.html'
    todo = TodoList.objects.all()
    return render(request, template_name, {'todos': todo})

def update_view(request, id):
    template_name = 'edit.html'
    form = TodoForm()
    obj = get_object_or_404(TodoList,id=id) 
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todo:todo_view'))
    
    return render(request, template_name, {'form':form})


def delete_view(request, id):
    template_name = 'delete.html'
    todo = TodoList.objects.get(id=id)
    if request.method == 'POST':
        todo.delete()
        return HttpResponseRedirect(reverse('todo:todo_view'))
    
    return render(request, template_name, {'todos':todo})