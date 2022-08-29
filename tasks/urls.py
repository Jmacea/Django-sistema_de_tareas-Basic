from django.urls import path
from .views import list_tasks, create_task, delete_task #importamos las funciones de views



urlpatterns = [
    path('',list_tasks),
    path('nuevo/',create_task, name='create_task'),#añadimos la url new y nnuestro metodo create_task y le ponemos un nombre en caso de que se modifique se muestre en el fron-ent con el url que se le coloque
    path('delete_task/<int:task_id>/',delete_task, name='delete_task'),
] 