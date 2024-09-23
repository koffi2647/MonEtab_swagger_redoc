from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.models.absence_model import AbsenceModel
from student.forms.absence_form import AbsenceForm



@login_required()
def add_abs(request):
    context={"title":"Ajout Absence"}

    if request.method == "POST":
        print(request.POST)
        absence_form =AbsenceForm(request.POST)
        context["absence_form"] = absence_form
        if absence_form.is_valid():
            print("form is valid")
            print(absence_form.cleaned_data)
            absence_form.save()
            return redirect('student:list_abs')
        else:
            return render(request,"student/absence.html")

    # context={'elev_form':elev_form}
    absence_form = AbsenceForm()
    context["absence_form"] = absence_form

    return render(request,"student/absence.html",context)


@login_required()
def list_abs(request):

    absences = AbsenceModel.objects.all()

    absence_count = AbsenceModel.objects.count()

    context = {
        'absences':absences,
        'absence_count':absence_count 
    }

    return render(request, "student/list_abs.html", context)


@login_required()
def update_abs(request,id):

    absence = AbsenceModel.objects.get(id = id)
    
    context={"title":"Modifier Absence"}

    if request.method == "POST":
        print(request.POST)
        absence_form =AbsenceForm(request.POST, instance = absence)
        context["absence_form"] = absence_form
        if absence_form.is_valid():
            print("form is valid")
            print(absence_form.cleaned_data)
            absence_form.save()
            return redirect('student:list_abs')
        else:
            return render(request,"student/absence.html")

    # context={'elev_form':elev_form}
    absence_form = AbsenceForm( instance = absence)

    context["absence_form"] = absence_form

    return render(request,"student/absence.html",context)
