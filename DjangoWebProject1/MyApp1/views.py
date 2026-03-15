from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import teacher
from .models import courseArea
from .forms import InputForm


# Create your views here.
def index(request):
    teach = teacher.objects.all()
    areas = list(courseArea.objects.values_list('courseArea', flat=True).distinct())
    print(areas)
    return render(request, "MyApp1/index.html", {'content' : teach, 'areas': areas})

def input_view(request):

    if request.method == "POST":

        form = InputForm(request.POST)



        if form.is_valid():

            form.save()

            return redirect("index")

    else:

        form = InputForm()



    return render(request, "MyApp1/input.html", {"form": form})