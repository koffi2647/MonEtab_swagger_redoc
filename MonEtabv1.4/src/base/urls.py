from django.urls import path
from .views import add


app_name="adress"
urlpatterns = [
    path('add',add,name="add"),
    # path('update/<int:id>',update,name="update-student"),
    # path('delete/<int:id>',delete,name="delete-student"),
]