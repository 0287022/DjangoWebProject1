from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import teacher, courseDescription, courseArea
from .models import courseArea
from .forms import InputForm, GenerateForm
# Create your views here.
def index(request):
    teach = teacher.objects.all()
    return render(request, "MyApp1/index.html", {'content' : teach})

def input_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = InputForm()
    return render(request, "MyApp1/input.html", {"form": form})

def generate_view(request):
    descs = courseDescription.objects.all()
    current_course = -1
    if request.method == "POST":
        form = GenerateForm(request.POST)
        if form.is_valid():
            current_course = int(request.POST.get('dropdown')) - 1
            print(current_course)
            if current_course == -1: return render(request, "MyApp1/generate.html", {"form": form})
            return render(request, "MyApp1/generate.html", {"form": form, 'descs': descs[current_course]})
    else:
        form = GenerateForm()
    return render(request, "MyApp1/generate.html", {"form": form})