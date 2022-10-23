from asyncio.windows_events import NULL
from datetime import datetime
from enum import unique
from sre_constants import IN
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import AbstractUser
from django .urls import reverse

from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class User(AbstractUser):
    # username, password, first_name. last_name, email are provided in AbstractUser model
     
     VICTIM='victim'
     POLICE='police'
     

     user_types=[
        (VICTIM, 'victim'),
        (POLICE,'police')
     ]
     phone_number = PhoneNumberField(unique=True, blank=True, null=True)
     #gender = models.CharField(max_length=5000)
     user_type=models.CharField(max_length=20, choices=user_types,null=True)

     class Meta:
        ordering=['first_name','last_name']
     def get_absolute_url(self):
          """Return the url to access a particular user"""
          return reverse('user-details', args=[str(self.id)])

     def __str__(self):
        return f'{self.first_name} {self.last_name}'

     def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
 
class Victim(models.Model):
   """Model representing a system user who's
    a victim"""
   user = models.OneToOneField(User, on_delete=CASCADE, primary_key=True, related_name='victim')
   
   dateofBirth = models.DateField(max_length=100,blank=True, null=True)
   social_status = models.CharField(max_length=5000,blank=True, null=True)
   location = models.CharField(max_length=200,blank=True, null=True) # street code
   relation_with_perpetrator =models.CharField(max_length=200,blank=True, null=True)

   def __str__(self):
      #return f'{self.user}'
      return self.user  
     
class Police(models.Model):
   """Model representing a user who's a police"""
   user = models.OneToOneField(User, on_delete=CASCADE, primary_key=True, related_name='police')
   police_id = models.FloatField(max_length=50, blank=True, null=True)
   station_number = models.FloatField(max_length=50,blank=True, null=True)
   location = models.CharField(max_length=200,blank=True, null=True) # street code
   


   def __str__(self):
      #return f'{self.user}'  
      return self.user  

class OffenceCategory(models.Model):
   """Model representing an offence category. 
   Offence categories are added by the Admin in the database. """
   name = models.CharField(max_length=200, help_text='Select a category (EG: Sexual Assault)')
   
   def __str__(self):
      return self.name

class Report(models.Model):
    
    
    offence_category = models.ForeignKey(
      OffenceCategory, 
      on_delete=SET_NULL, 
      null=True, 
      help_text='Select the offence category.',
      )
    datetime = models.DateField(max_length=5000,blank=True,null=True)
    county = models.CharField(max_length=500,blank=True,null=True)
    where_committed = models.CharField(max_length=200,blank=True,null=True) # street code
    any_other_message = models.CharField(max_length=500,blank=True,null=True)
    Perpetrator_Full_names = models.CharField(max_length=5000,blank=True,null=True)
    Perpetrator_Phone_Number = models.FloatField(max_length=500,blank=True,null=True)
    Relationship_with_perpetrator = models.CharField(max_length=500,blank=True,null=True)
    
    
   
    
    

    def __str__(self):
      return f'{self.user}: {self.offence_category}'





     


    


class PoliceProfileImageUpload(models.Model):
   """Model representing a police's profile picture upload"""
   police = models.ForeignKey(User,related_name='police_image', on_delete=models.CASCADE)
   image = models.ImageField(upload_to='police_img_uploads')
   

   def __str__(self):
      return f"{self.police.user}'s image" 

   


   class TrackStatus(models.Model):
    """Model representing the tracking update"""
   PENDING = 'Pending'
   COMPLETED = 'Completed'
   IN_PROGRESS = 'In_progress'

   STATUS_CHOICES = [
      (PENDING, 'Pending'),
      (COMPLETED, 'Completed'),
      (IN_PROGRESS, 'In_Progress'),
   ]

