from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('',views.contact, name='contact'),
    path('',views.about, name='about'),
    path('',views.offence, name='offence'),
    path('',views.perpetrator, name='perepetrator'),
   
    

    
]