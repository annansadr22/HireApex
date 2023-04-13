from django.shortcuts import render,redirect
from .models import Rating
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField

from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def user_list(request):
    users = User.objects.all()
    ratings = {}
    for user in users:
        rating_objects = Rating.objects.filter(user=user)
        if rating_objects:
            rating_sum = sum(rating.rating for rating in rating_objects)
            average_rating = rating_sum / len(rating_objects)
            ratings[user.id] = round(average_rating, 2)
        else:
            ratings[user.id] = None
    context = {'users': users, 'ratings': ratings}
    return render(request, 'user_list.html', context)



def rate_user(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        rating = int(request.POST['rating'])
        Rating.objects.create(user=user, rating=rating)
        return redirect('user_list')
    else:
        return render(request, 'rate_user.html', {'user': user})
