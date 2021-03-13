from django.urls import path

from . import views

urlpatterns = [
    path('detail/<int:id>', views.detail, name='detail'),
    path('list', views.index, name='index'),
    path('add', views.addNew, name='add'),
    path('update<int:id>', views.updatetask, name='update'),
    path('delete<int:id>', views.delete, name='delete'),
    path('done<int:id>', views.active, name='done'),
]
