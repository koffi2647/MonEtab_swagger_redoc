from django.urls import path
from .views import index, check_setting



app_name="dashboard"

urlpatterns = [
    path('', check_setting, name="check_setting"),
    path('index/', index, name='index'),
]