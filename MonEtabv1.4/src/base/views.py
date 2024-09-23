from django.shortcuts import render, redirect
from .forms import AdressFoms

# Create your views here.
def add(request):
    context={"title":"Ajouter Adress"}

    if request.method == "POST":
        print(request.POST)
        form =AdressFoms(request.POST)
        context["form"] = form
        if form.is_valid():
            print("form is valid")
            print(form.cleaned_data)
            form.save()
            return redirect('student:index')
        else:
            return render(request,"base/adress.html")

    # context={'elev_form':elev_form}
    form = AdressFoms()
    context["form"] = form

    return render(request,"base/adress.html",context)
