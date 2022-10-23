from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'general/home.html')

def contact (request):
    return render(request, 'general/contact.html')

def about(request):
    return render(request, 'general/about.html')

def register(request):
    return render(request, 'general/register.html')

    
def offence (request):
    return render(request, 'victim/offence.html')


