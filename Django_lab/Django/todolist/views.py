from django.shortcuts import render, redirect

# Create your views here.
from todolist.models import Todolist


def index(request):
    todolist = Todolist.objects.all()
    return render(request, "index.html", {
        "tasks": todolist,
        "name": "List Of New Tasks",
    })


def detail(request, id):
    todo = Todolist.objects.get(id=id)
    return render(request, "detail.html", {
        "tasks": todo,
        "name": "Detail Of New Task",
    })


def addNew(request):
    if request.method == "POST":
        name = request.POST['task']
        description = request.POST['description']
        priority = request.POST['priority']
        Todolist.objects.create(name=name, description=description, priority=priority)
        return redirect("index")

    return render(request, "addnewtask.html")


def updatetask(request, id):
    if request.method == "POST":
        task = Todolist.objects.get(id=id)
        if request.POST['task']:
            task.name = request.POST['task']
        if request.POST['description']:
            task.description = request.POST['description']
        if request.POST['priority']:
            task.priority = request.POST['priority']
        task.save()
        return redirect("index")
    todo = Todolist.objects.get(id=id)
    return render(request, "update.html", {
        "tasks": todo,
        "name": "Detail Of New Task",
    })


def delete(request, id):
    todo = Todolist.objects.get(id=id)
    todo.delete()
    return redirect("index")


def active(request, id):
    task = Todolist.objects.get(id=id)
    task.active = True
    task.save()
    return redirect("index")
