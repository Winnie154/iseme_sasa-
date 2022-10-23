from django.shortcuts import render
from django.http import HttpResponse

#from setup.iseme_sasa.models import Report

# Create your views here.
Report = [
    {
        'Name': 'John Monroe',
        'Mobile_number': '0722781493',
        'county': 'Nairobi',
        'date': 'August 27, 2022'
    },
    {
        'Name': 'Mary Becky',
        'Mobile_number': '0717654970',
        'county': 'Nakuru',
        'date': 'September 14, 2022'
    }
]

def home(request):
     context = {
        'report': Report
     }
     return render(request, 'general/home.html', context)
     

def contact (request):
    return render(request, 'general/contact.html', )

def about(request):
    return render(request, 'general/about.html', {'title': 'About'})

def register(request):
    return render(request, 'general/register.html')

    
def offence (request):
    return render(request, 'victim/offence.html')


