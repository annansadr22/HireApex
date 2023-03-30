from django.shortcuts import render,redirect
from .models import UserProfile,JobProfile,SkillSet,Language
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField
from .forms import MyModelForm
from django.urls import reverse_lazy


# Create your views here.

# class UserProfileCreate(CreateView):
#     model = UserProfile
#     form_class = UserProfileForm
#     # if form_class.is_valid():
#     #     form_class.save()

#     template_name = 'land/UserProfile_form.html'
#     success_url = reverse_lazy('home')


# def UserProfileCreate(request):
#     form=UserProfileForm
#     if request.method=='POST':
#         form=UserProfileForm(request.POST)
#         if form.is_valid():
#             print("VALID")
#             form.save()
#             #return redirect('/')

#     context ={'form':form}
    
#     return render(request,'land/UserProfile_form.html',context)


# class UserProfileCreate(CreateView):
#     template_name = 'land/UserProfile_form.html'
#     form_class = MyModelForm
#     success_url = '/home/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class UserProfileCreate(CreateView):
    # skills = ModelMultipleChoiceField(queryset=SkillSet.objects.all())
    # language = ModelMultipleChoiceField(queryset=Language.objects.all())
    model = UserProfile
    fields = [ 'full_name', 'profile_picture','money_per_hour','language','skills']
    # widgets = {
    #         'language': forms.Select(),
    #         'skills': forms.CheckboxSelectMultiple()
    #     }
    # language = forms.ModelMultipleChoiceField(
    #     queryset=Language.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    # skills = forms.ModelMultipleChoiceField(
    #     queryset=SkillSet.objects.all(),
    #     widget=forms.CheckboxSelectMultiple
    # )
    widgets = {
            'language': forms.CheckboxSelectMultiple()
        }
    success_url = reverse_lazy('home')

    
    def form_valid(self, form):
        form.instance.username = self.request.user.username
        return super().form_valid(form)
    

class UserProfileListView(ListView):
    queryset=UserProfile.objects.all()
    
    
class JobProfileCreate(CreateView):
    model = JobProfile
    fields = [ 'job_name', 'job_description','duration_of_employment','money_hr']

