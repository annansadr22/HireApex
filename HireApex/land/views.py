from django.shortcuts import render
from .models import UserProfile,JobProfile,SkillSet,Language
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.

class UserProfileCreate(CreateView):
    model = UserProfile
    fields = [ 'full_name', 'profile_picture','money_per_hour']

    
    def form_valid(self, form):
        form.instance.username = self.request.user.username
        return super().form_valid(form)

    
class JobProfileCreate(CreateView):
    model = JobProfile
    fields = [ 'job_name', 'job_description','duration_of_employment','money_hr']

