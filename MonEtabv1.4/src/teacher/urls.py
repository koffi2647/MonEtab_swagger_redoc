from django.urls import path
from .views import index, add, update, delete, check_setting



app_name="teacher"

urlpatterns = [
    path('', check_setting, name='check_setting'),
    path('index', index,name="index"),
    path('add',add,name="add"),
    path('update/<int:id>',update,name="update-teacher"),
    path('delete/<int:id>',delete,name="delete-teacher"),
]