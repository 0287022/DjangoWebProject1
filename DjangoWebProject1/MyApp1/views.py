from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import teacher
from .models import courseArea
from .forms import InputForm, GenerateForm

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table
from django.http import FileResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from io import BytesIO


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
    areas = list(courseArea.objects.all())
    if request.method == "POST":
        form = GenerateForm(request.POST)
        if form.is_valid():
            answer = (request.POST.get('dropdown'))
            print(answer)
            return redirect("generate")
    else:
        form = GenerateForm()
    return render(request, "MyApp1/generate.html", {"form": form})

def generate_pdf():
    buffer = BytesIO()
    p = canvas.Canvas(buffer)
    lines = ['Name', 'Teaching Area']

    teachers = teacher.objects.all()
    for teach in teachers:
        lines.append((teach.Name, teach.Area))
    table = Table(lines)
    table.wrapOn(p, 300, 300)
    table.drawOn(p, 0, 5)

    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

def report(request):
    pdf_file = staticfiles_storage.path("DigitalSolutions.pdf")
    try:
        merger = PdfWriter()
        input1 = PdfReader(generate_pdf())
        input2 = PdfReader(pdf_file, 'rb')

        merger.append(input1)
        merger.append(input2)

        buffer = BytesIO()
        merger.write(buffer)
        buffer.seek(0)

        response = FileResponse(buffer, as_attachment = True, filename="awawa!!.pdf")

    except FileNotFoundError:
        response = FileResponse(generate_pdf(), as_attachment = True, filename="awawa_:(.pdf")

    return response