from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Todo
from .forms import TodoForm


# Create your views here.
def home(request):
    return render(request, 'home.html')


def currenttodos(request):
    todos = Todo.objects.filter(completed=False)
    content = {'todos': todos}
    return render(request, 'currenttodos.html', content)

def completetodos(request):
    todos = Todo.objects.filter(completed=True)
    content = {'todos': todos}
    return render(request, 'completetodos.html', content)


def alltodos(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'alltodos.html', content)


def createtodo(request):
    if request.method == 'GET':
        content = {'form': TodoForm()}
        return render(request, 'createtodo.html', content)
    else:
        form = TodoForm(request.POST)
        form.save()
        return redirect('currenttodos')


def viewtodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        content = {'todo': todo,
                   'form': form}
        return render(request, 'viewtodo.html', content)
    else:
        form = TodoForm(request.POST, instance=todo)
        todo.completed_date = None if todo.completed else timezone.now()
        form.save()
        return redirect('currenttodos')


def completetodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.completed_date = timezone.now()
        todo.completed = True
        todo.save()
        return redirect('alltodos')


def continuetodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.completed_date = None
        todo.completed = False
        todo.save()
        return redirect('alltodos')


def deletetodo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('alltodos')