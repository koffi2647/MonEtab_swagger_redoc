from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeacherFoms
from user.models.appSetting_model import AppSettingModel
from .models.teacher_model import TeacherModel

# Create your views here.
@login_required
def index(request):

    search_field = request.GET.get('search')

    if search_field:

        teachers = TeacherModel.objects.filter(last_name__icontains = search_field)

        teacher_count = TeacherModel.objects.count()

        context = {
            'teachers': teachers,
            'teacher_count': teacher_count
        }
    else:
        teachers = TeacherModel.objects.all()
        teacher_count = TeacherModel.objects.count()
        context = {
            'teachers': teachers,
            'teacher_count': teacher_count
        }   
    return render(request, "teacher/index.html", context)


@login_required()
def add(request):
    context={"title":"Ajouter un eleve"}

    if request.method == "POST":
        print(request.POST)
        form = TeacherFoms(request.POST)
        context["form"] = form
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('teacher:index')
        else:
            return render(request,"teacher/add.html")
    
    # context={'teach_form': teach_form}
    form = TeacherFoms()
    context["form"] = form

    return render(request,"teacher/add.html",context)


@login_required()
def update(request, id):
    teacher = TeacherModel.objects.get(id=id)

    context = {"title":"Modifier professeur"}

    if request.method == "POST":
        form = TeacherFoms(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
        
    form = TeacherFoms(instance = teacher)

    context["form"] = form
    
    return render(request,"teacher/add.html",context)


@login_required()
def delete(request, id):
    teacher = TeacherModel.objects.get(id = id)
    teacher.delete()
    return redirect('teacher:index')



def check_setting(request):
    app_setting  = AppSettingModel.objects.all()

    if not app_setting:
        return redirect('user:appS')
    else:
        return redirect('user:check_school')
