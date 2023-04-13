from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
    
    username = models.CharField(primary_key=True, max_length=50)
    full_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100,default=None)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    money_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    language = models.ManyToManyField('Language')
    skills = models.ManyToManyField('SkillSet')
    #time_spent_on_web = models.DurationField()
    job_created=models.ManyToManyField('JobProfile')

    def __str__(self):
        return self.username
    # def get_absolute_url(self): 
    #     return reverse('home')
    

class JobProfile(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=600)
    duration_of_employment = models.IntegerField()
    money_hr = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.job_name
    def get_absolute_url(self):
        return reverse('home')








class Language(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    

    def __str__(self):
        return self.name
    

class SkillSet(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    

    def __str__(self):
        return self.name


