from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def list_tasks(request):
    tasks = Task.objects.all()#de esta forma mandamos a llamar los objetos de la clase Task
    return render(request, 'list_tasks.html', {"tasks": tasks})

def create_task(request):#creamos el metodo de craer tareas
    task = Task(title=request.POST['title'], description=request.POST['description'])#creamos un objeto que viene de la clase modelo que creamos con los parametros y llamamos al metodo reques.POST
    task.save()#lo guardamos
    return redirect('/tasks/')#que nos redirija a /tasks

def delete_task(request, task_id):
    dele_task= Task.objects.get(id=task_id)#de esta forma creamos encontramos el objeto
    dele_task.delete()#eliminamos el objeto
    return redirect('/tasks/')