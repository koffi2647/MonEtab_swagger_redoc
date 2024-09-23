from django.urls import path
from .views.student_view import index,add, update, delete, check_setting
from .views.absence_view import add_abs,list_abs, update_abs 
from .views.studentCards_view import add_card, list_card, update_student_card



app_name="student"
urlpatterns = [

    path('', check_setting, name='check_setting'),

    path('index', index,name="index"),
    path('add',add,name="add"),
    path('update/<int:id>',update,name="update-student"),
    path('delete/<int:id>',delete,name="delete-student"),

    path('add_abs',add_abs,name="add_abs"),
    path('list_abs',list_abs,name="list_abs"),
    path('update_abs/<int:id>',update_abs,name="update_absence"),

    path('add_card',add_card,name="add_card"),
    path('list_card',list_card,name="list_card"),
    path('update_student_card/<int:id>', update_student_card, name='update_student_card')
]