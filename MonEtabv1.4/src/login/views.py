from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from user.models.appSetting_model import AppSettingModel
from user.models.custom_user_model import CustomUserModel
from django.contrib import messages


# Create your views here.
def sign_in(request):

    #if CustomUserModel.is_authenticated:
     #   return redirect('dashboard:index')
    
    # next_url = request.GET.get('next','')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        #next = request.GET.get('next')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            # print(next_url)

            login(request, user)
            # if next:
            #     return redirect(next)
            return redirect('dashboard:index')
            
            #return redirect('user:list')
        else:
            messages.error(request, "Nom utilisateur ou mot de passe incorect.")

    return render(request, 'login/sign_in.html')

def sign_up(request):

    if request.method == 'POST':
        username = request.POST.get('pseudo', '')
        password = request.POST.get('password', '')

        if not username or not password:
            return render(request,'login/sign_up.html')
        
        user = CustomUserModel(username=username)
        user.save() 

        user.password = password
        user.set_password(user.password)
        user.save()
        # login(request,user)
        return redirect('login:sign_in')

    return render(request, 'login/sign_up.html')


@login_required()
def log_out(request):
    request(logout)
    return redirect('login:sign_in')


def check_setting(request):
    app_setting = AppSettingModel.objects.all()

    if not app_setting:
        return redirect('user:appS')
    else:
        return redirect('user:check_school')
