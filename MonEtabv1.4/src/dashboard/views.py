from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.models.student_model import StudentModel
from teacher.models.teacher_model import TeacherModel
from user.models.custom_user_model import CustomUserModel
from user.models.appSetting_model import AppSettingModel



# Create your views here.
@login_required
def index(request):
    nb_student = StudentModel.objects.count()
    nb_teacher = TeacherModel.objects.count()
    nb_user = CustomUserModel.objects.count()
    context = {
        'nb_student': nb_student,
        'nb_teacher': nb_teacher,
        'nb_user': nb_user,
    }
    return render(request,"dashboard/index.html",context)


def check_setting(request):
    app_setting = AppSettingModel.objects.all()

    if not app_setting:
        return redirect('user:appS')
    else:
        return redirect('user:check_school')