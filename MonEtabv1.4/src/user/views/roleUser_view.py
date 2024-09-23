from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms.roleUser_form import RoleUserForm
from user.models.roleUser_model import RoleUserModel
from user.models.appSetting_model import AppSettingModel

def index_role(request):
    roles = RoleUserModel.objects.all()
    role_count = RoleUserModel.objects.count()
    context = {
        'roles':roles,
        'role_count':role_count
        
    }
    return render(request, "user/list_role.html", context)


def role(request):

    context={"title":"Ajout Role"}

    if request.method == "POST":
        print(request.POST)
        user_role_form =RoleUserForm(request.POST)
        context["user_role_form"] = user_role_form
        if user_role_form.is_valid():
            print("form is valid")
            print(user_role_form.cleaned_data)
            user_role_form.save()
            return redirect('user:check_user')
        else:
            return render(request,"user/roleUser.html")

    # context={'elev_form':elev_form}
    user_role_form = RoleUserForm()
    context["user_role_form"] = user_role_form

    role_users = RoleUserModel.objects.all()

    if not role_users:
        return render(request,"user/roleUser.html",context)
    else:
        return redirect('user:check_user')



def role_update(request, id):

    role_user = RoleUserModel.objects.get(id = id)

    context={"title":"Update Role"}

    if request.method == "POST":
        print(request.POST)
        user_role_form =RoleUserForm(request.POST, instance = role_user)
        context["user_role_form"] = user_role_form
        if user_role_form.is_valid():
            print("form is valid")
            print(user_role_form.cleaned_data)
            user_role_form.save()
            return redirect('user:index_role')
        else:
            return render(request,"user/roleUser.html")

    # context={'elev_form':elev_form}
    user_role_form = RoleUserForm(instance = role_user)
    
    context["user_role_form"] = user_role_form

    return render(request,"user/roleUser.html",context)


def check_role_user(request):

    role_users = RoleUserModel.objects.all()

    if not role_users:
        return redirect('user:role')
    else:
        return redirect('user:check_user')
    


def check_setting(request):
    app_setting  = AppSettingModel.objects.all()

    if not app_setting:
        return redirect('user:appS')
    else:
        return redirect('user:check_school')
