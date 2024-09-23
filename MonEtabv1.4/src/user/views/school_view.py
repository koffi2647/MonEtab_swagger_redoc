from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user.forms.school_form import SchoolForm
from user.models.school_model import SchoolModel



def school(request):

    if request.user.is_authenticated:
        return redirect('dashboard:index')

    context = {
        "title": "School Setting"
    }

    if request.method == "POST":
        print(request.POST)
        form_school = SchoolForm(request.POST)
        context["form_school"] = form_school
        if form_school.is_valid():
            print("form is valid")
            print(form_school.cleaned_data)
            form_school.save()
            return redirect('user:check_role_user')
        else:
            return render(request,"user/school.html")

    # context={'elev_form':elev_form}
    form_school = SchoolForm()
    
    context['form_school'] = form_school

    schools = SchoolModel.objects.all()

    if not schools:
        return render(request,"user/school.html",context)
    else:
        return redirect('login:sign_in')



@login_required()
def edition(request):

    school = SchoolModel.objects.first()

    context = {
        'title': 'Edit School'
    }

    if request.method == 'POST':
        form_school = SchoolForm(request.POST, instance = school)
        if form_school.is_valid():
            form_school.save()
            return redirect('dashboard:index')
    else:
        form_school = SchoolForm(instance=school)

    context['form_school'] = form_school

    return render(request, 'user/school.html', context)



def check_school(request):
    schools = SchoolModel.objects.all()

    if not schools:
        return redirect('user:school')
    else:
        return redirect('user:check_role_user')
