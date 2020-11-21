from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone


from .models import Todo


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-date_added')
    context = {
        'todo_items': todo_items
    }
    return render(request, 'base.html', context)


def add_todo(request):
    content = request.POST['todo']
    Todo.objects.create(todo=content)
    return redirect(reverse('sanity:index'))


def delete_todo(request, todo_id):
    Todo.objects.get(pk=todo_id).delete()
    return redirect(reverse('sanity:index'))
