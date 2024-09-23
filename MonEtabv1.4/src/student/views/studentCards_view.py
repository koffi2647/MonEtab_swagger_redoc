from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from student.forms.studentCards_form import StudentCardFoms
from student.models.studentCards_model import StudentCardsModel


@login_required()
def add_card(request):
    context={"title":"Carte Etudiant"}

    if request.method == "POST":
        print(request.POST)
        student_card_form =StudentCardFoms(request.POST)
        context["student_card_form"] = student_card_form
        if student_card_form.is_valid():
            print("form is valid")
            print(student_card_form.cleaned_data)
            student_card_form.save()
            return redirect('student:list_card')
        else:
            return render(request,"student/studentCards.html")


    student_card_form = StudentCardFoms()

    context["student_card_form"] = student_card_form

    return render(request,"student/studentCards.html",context)


@login_required()
def list_card(request):
    studentCardss = StudentCardsModel.objects.all()
    carte_count = StudentCardsModel.objects.count()
    context = {
        'studentCardss':studentCardss,
        'carte_count':carte_count
        
    }
    return render(request, "student/list_card.html", context)


@login_required()
def update_student_card(request, id):

    student_card = StudentCardsModel.objects.get(id = id)

    context={"title":"Carte Etudiant"}

    if request.method == "POST":
        print(request.POST)
        student_card_form =StudentCardFoms(request.POST, instance = student_card)
        context["student_card_form"] = student_card_form
        if student_card_form.is_valid():
            print("form is valid")
            print(student_card_form.cleaned_data)
            student_card_form.save()
            return redirect('student:list_card')
        else:
            return render(request,"student/studentCards.html")


    student_card_form = StudentCardFoms(instance = student_card)
    
    context["student_card_form"] = student_card_form

    return render(request,"student/studentCards.html",context)
