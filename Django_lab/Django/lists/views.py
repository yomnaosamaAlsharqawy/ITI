from django.shortcuts import render, redirect

# Create your views here.
tasks = []


def index(request):
    return render(request, "list.html", {
        "tasks": tasks,
        "name": "List Of New Tasks",
    })


def addNew(request):
    if request.method == "POST":
        task = request.POST['task']
        tasks.append(task)
        return redirect("index")

    return render(request, "addnew.html")
