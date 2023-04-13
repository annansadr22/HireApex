from django.shortcuts import render,redirect
from .models import UserProfile,JobProfile,SkillSet,Language
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField
from .forms import MyModelForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect




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
    fields = [ 'full_name', 'profile_picture','money_per_hour','bio','language','skills']
    template_name_suffix="_form"
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
    def get_object(self):
        return UserProfile.objects.get(pk=self.request.POST.get("pk"))

class UserProfileListView(ListView):
    queryset=UserProfile.objects.all()
    

class JobProfileCreate(CreateView):
    model = JobProfile
    fields = [ 'job_name', 'job_description','duration_of_employment','money_hr']



class JobProfileListView(ListView):
    queryset=JobProfile.objects.all()
    template_name = 'land/search.html'


from django.db.models import Q

def search(request):
    if 'q' in request.GET:
        query = request.GET['q']
    results = JobProfile.objects.filter(Q(job_name__icontains=query) | Q(job_description__icontains=query)).distinct()
    context = {'results': results, 'query': query}
    return render(request, 'land/searching.html', context)
