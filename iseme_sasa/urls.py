from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
    path('register',views.register, name='register'),
    path('ffence',views.offence, name='offence'),
    path('perpetrator',views.perpetrator, name='perepetrator'),
   
    

    
]