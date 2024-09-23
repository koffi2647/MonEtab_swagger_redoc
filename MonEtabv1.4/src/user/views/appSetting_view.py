from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms.appSetting_form import AppSettingForm
from user.models.appSetting_model import AppSettingModel



def appS(request):

    if request.user.is_authenticated:
        return redirect('dashboard:index')

    context={"title":"App setting"}

    if request.method == "POST":
        print(request.POST)
        app_setting_form =AppSettingForm(request.POST)
        if app_setting_form.is_valid():
            print("form is valid")
            print(app_setting_form.cleaned_data)
            app_setting_form.save()
            return redirect('user:check_school')
        else:
            return render(request,"user/appSetting.html")

    app_setting_form = AppSettingForm()
    context["app_setting_form"] = app_setting_form

    app_setting  = AppSettingModel.objects.all()

    if not app_setting:
        return render(request,"user/appSetting.html",context)
    else:
        return redirect('user:school')



@login_required()
def edition_setting(request):

    app_setting = AppSettingModel.objects.first()

    context = {
        'title': 'Edit App Settings'
    }

    if request.method == "POST":
        print(request.POST)
        app_setting_form =AppSettingForm(request.POST, instance = app_setting)
        if app_setting_form.is_valid():
            print("form is valid")
            print(app_setting_form.cleaned_data)
            app_setting_form.save()
            return redirect('user:index_ap')
        else:
            return render(request,"user/appSetting.html")

    app_setting_form = AppSettingForm(instance = app_setting)
    context["app_setting_form"] = app_setting_form

    return render(request,"user/appSetting.html",context)




def check_setting(request):
    app_setting  = AppSettingModel.objects.all()

    if not app_setting:
        return redirect('user:appS')
    else:
        return redirect('user:check_school')