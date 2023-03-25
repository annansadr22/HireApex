from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('', TemplateView.as_view(template_name='dashboard/home.html'),name='home'),
    path('faq/', TemplateView.as_view(template_name='extra/faq.html'),name='faq'),
    path('contact-us/', TemplateView.as_view(template_name='extra/contactus.html'),name='contact_us'),
    path('form-job/', views.JobProfileCreate.as_view(),name='form_job'),
    path('form-freelance/', views.UserProfileCreate.as_view(),name='form_freelance'),
    
]