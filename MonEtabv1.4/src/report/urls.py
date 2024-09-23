from django.urls import path
from .views import check_setting, index, export



app_name = 'report'

urlpatterns = [
    path('', check_setting, name='check_setting'),
    path('index/', index, name='index'),
    path('generate/', export, name='generer')
]
