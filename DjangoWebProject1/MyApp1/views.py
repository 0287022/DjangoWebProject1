from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    return render(
        request,
        "MyApp1/index.html",
        {
            'content' : "Hello Django! Said on ",
            'time' : now.strftime("%A, %d %B, %Y at %X"),
            'title' : ':3'
        }
    )
