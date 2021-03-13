from django.urls import path

from . import views

urlpatterns = [
    path('addnew', views.addNew, name='add'),
    path('list', views.index, name='index'),
]
