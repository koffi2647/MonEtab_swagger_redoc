from django.urls import path
from .views.user_view import index, add, update, check_user, sign_out, desable_user
from .views.appSetting_view import  appS, check_setting, edition_setting
from .views.school_view import school, check_school, edition
from .views.roleUser_view import role, index_role, role_update, check_role_user


app_name="user"
urlpatterns = [

    path('', check_setting, name='check_setting'),

    path('dashboard/', index,name="index"),
    path('desable/<int:id>', desable_user, name='desable_user'),
    path('checkuser', check_user, name='check_user'),
    path('add',add,name="add"),
    path('update/<int:id>',update,name="update-user"),

    path('checkschool', check_school, name='check_school'),
    path('school',school,name="school"),
    path('edition_school', edition, name='edition_school'),

    path('role',role,name="role"),
    path('checkroleuser', check_role_user, name='check_role_user'),
    path('index_role',index_role,name="index_role"),
    path('update_user_role/<int:id>',role_update, name='update_user_role'),
    

    path('appS',appS,name="appS"),
    path('edittion',edition_setting,name="edition_setting"),


    
    path('signout', sign_out, name='sign_out'),
    
    #path('delete/<int:id>',delete,name="delete-student"),
]