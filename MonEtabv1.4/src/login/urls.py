from django.urls import path
from .views import sign_in, sign_up, log_out, check_setting



app_name = 'login'

urlpatterns = [
    path('', check_setting, name='check_setting'),
    path('sign_in/', sign_in, name='sign_in'),
    path('log_out/', log_out, name='log_out'),
    path('register/', sign_up, name='sign_up')
]