from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request, name):
    return HttpResponse(f"<h1>HELLO, {name}!</h1>")
