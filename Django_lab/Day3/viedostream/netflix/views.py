# Create your views here.
from django.shortcuts import redirect, render

from netflix.forms import MovieForm
from netflix.models import Movies
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def index(request):
    movies = Movies.objects.all()
    return render(request, "index.html", {
        "movies": movies,
        "name": "List Of Movies",
    })

@login_required
def show(request, id):
    movie = Movies.objects.get(id=id)
    categories = movie.category.all()
    return render(request, "detail.html", {
        "movie": movie,
        "categories": categories,
        "name": "Detail Of New Task",
    })


@login_required
@permission_required('netflix', raise_exception=True)
def create(request):
    form = MovieForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "create.html", {
        'form': form
    })


@login_required
@permission_required('netflix', raise_exception=True)
def delete(request, id):
    movie = Movies.objects.get(id=id)
    movie.delete()
    return redirect("index")


@login_required
@permission_required('netflix', raise_exception=True)
def update(request, id):
    movie = Movies.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "update.html", {
        'form': form,
        'movie': movie
    })
