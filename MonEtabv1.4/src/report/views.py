from django.shortcuts import render, redirect
import openpyxl
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from user.models.custom_user_model import CustomUserModel
from django.contrib.auth.decorators import login_required
from teacher.models.teacher_model import TeacherModel
from student.models.student_model import StudentModel
from user.models.appSetting_model import AppSettingModel
from openpyxl import Workbook
from teacher.models.teacher_model import TeacherModel
from xhtml2pdf import pisa
from django.template.loader import render_to_string


# Create your views here.
@login_required
def index(request):
    return render(request, 'report/index.html')


@login_required()
def export(request):
    if request.method == 'POST':
        type = request.POST.get('type','')
        button = request.POST.get('button','')
        if button == 'pdf':
            return export_pdf(type)
        elif button == 'excel':
            return export_excel(type)


def export_excel(type):
    workbook = Workbook()
    sheet = workbook.active
    if type == "student":
        sheet.title = 'Students liste'

        sheet.append(['Matricule', 'Last name', 'First name', 'Number'])

        students = StudentModel.objects.all()
    
        for student in students:
            sheet.append([student.matricule, student.last_name, student.first_name , student.phone_number ])


        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'inline; filename=students.xlsx'

    elif type == "teacher":
        sheet.title = 'Teachers liste'

        sheet.append(['Last name', 'First name', 'Number'])

        teachers = TeacherModel.objects.all()
    
        for teacher in teachers:
            sheet.append([teacher.last_name, teacher.first_name , teacher.phone_number ])


        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=teachers.xlsx'

    elif type == "user":
        sheet.title = 'Users liste'

        sheet.append(['Username'])      

        users = CustomUserModel.objects.all()
    
        for user in users:
            sheet.append([user.username])


        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=users.xlsx'
    
    else:
        return redirect('report:index')
    
    workbook.save(response)
        
    return response
       

def export_pdf(type):

    if type == "student":
        students = StudentModel.objects.all()
    

        context = {
            'students': students,
        }
        html_content= render_to_string('report/pdf.html',context)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="students.pdf"'

    elif type == "teacher":
        teachers = TeacherModel.objects.all()
    

        context = {
            'teachers': teachers,
        }
        html_content= render_to_string('report/pdf.html',context)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="teachers.pdf"'

    elif type == "user":
        users = CustomUserModel.objects.all()
    

        context = {
            'users': users,
        }
        html_content= render_to_string('report/pdf.html',context)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="users.pdf"'
    
    else:
            return redirect('report:index')
    
    pisa_status = pisa.CreatePDF(html_content, dest=response)

    if pisa_status.err:
        return HttpResponse('An error occurred while generating the PDF', status=500)

    return response




def check_setting(request):
    app_setting  = AppSettingModel.objects.all()

    if not app_setting:
        return redirect('user:appS')
    else:
        return redirect('user:check_school')