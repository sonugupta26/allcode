from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        "students": [
            {"name": "Ram", "contact":"789456123", "addrersh": "ktm" },
            {"name": "Shyam", "contact":"99555123", "addrersh": "bkt" },
            {"name": "Sonu", "contact":"000456123", "addrersh": "ppp" }


        ]
    }
    return render(request, "home.html", context)
    
    
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def addresh(request):
    return render(request, "addresh.html")