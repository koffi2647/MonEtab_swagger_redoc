from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.forms.student_form import StudentFoms
from student.models.student_model import StudentModel
from user.models.appSetting_model import AppSettingModel


@login_required
def index(request):

    search_field = request.GET.get('search')

    if search_field:

        students = StudentModel.objects.filter(last_name__icontains = search_field)
        student_count = StudentModel.objects.count()

        context = {
            'students': students,
            'search_fields': search_field
        }
    else:
        students = StudentModel.objects.all()
        student_count = StudentModel.objects.count()
        context = {
            'students':students,
            'student_count': student_count
            
        }

    return render(request, "student/index.html", context)


@login_required()
def add(request):
    context={"title":"Ajouter Eleve"}

    if request.method == "POST":
        print(request.POST)
        form =StudentFoms(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('student:index')
        else:
            return render(request,"student/add.html")

    # context={'elev_form':elev_form}
    form = StudentFoms()
    context["form"] = form

    return render(request,"student/add.html",context)


@login_required()
def update(request, id ):
    student = StudentModel.objects.get(id=id)

    context = {"title":"Modifier eleve"}


    if request.method == "POST":
        form = StudentFoms(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:index')
        
    form = StudentFoms(instance = student)

    context["form"] = form

    return render(request,"student/add.html",context)


@login_required()
def delete(request ,id):
    student = StudentModel.objects.get(id = id)
    student.delete()
    return redirect('student:index')



def check_setting(request):
    app_setting  = AppSettingModel.objects.all()

    if not app_setting:
        return redirect('user:appS')
    else:
        return redirect('user:check_school')
