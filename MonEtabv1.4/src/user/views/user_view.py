from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from user.models.custom_user_model import CustomUserModel
from user.models.roleUser_model import RoleUserModel
from user.forms.user_form import UserFoms
from user.forms.roleUser_form import RoleUserForm


@login_required()
def index(request):

    search_field = request.GET.get('search')

    if search_field:
        users = CustomUserModel.objects.filter(username__icontains = search_field)

        context = {
            'users': users,
            'search_fields': search_field
        }
    else:     
        users = CustomUserModel.objects.all()
        print(users)
        user_count = CustomUserModel.objects.count()
        context = {
            'users':users,
            'user_count':user_count
        }
    return render(request, "user/index.html", context)



def add(request):
    context={"title":"Ajouter Utilisateur"}

    if request.method == "POST":
        print(request.POST)
        form = UserFoms(request.POST)
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = CustomUserModel(username = username)
            # user.save()

            # user.password = password
            # user.set_password(user.password)
            # user.save()

            return redirect('login:sign_in')            
        else:
            return render(request,"user/add.html")

    form = UserFoms()
    context = {
        'form': form
    }

    return render(request,"user/add.html",context)


@login_required()
def update(request, id):
    
    user = CustomUserModel.objects.get(id=id)
 
    context = {
        "title":"Modifier utilisateur"
    }

    if request.method == "POST":
        form = UserFoms(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:index')
        
    form = UserFoms(instance = user)

    context["form"] = form

    return render(request,"user/add.html",context)



def sign_out(request):
    logout(request)
    return redirect('login:sign_in')


def check_user(request):

    users = CustomUserModel.objects.all()

    if users:
        return redirect('dashboard:index')
    else:
        return redirect('user:add')
    


def desable_user(request, id):
    user = get_object_or_404(CustomUserModel, id = id)
    user.is_active = False
    user.status = False
    user.save()
    return redirect('user:index')