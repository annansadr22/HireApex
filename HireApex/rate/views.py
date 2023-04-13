from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Rating


def rate_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    value = int(request.POST.get('value'))
    rater = request.user
    if user != rater and not user.ratings_received.filter(rater=rater).exists():
        rating = Rating(user=user, value=value, rater=rater)
        rating.save()
    return redirect('user_detail', user_id=user_id)

def user_detail(request, user_id):
    user = get_object_or_404(User, id=user_id)
    ratings = Rating.objects.filter(user=user)
    rating_count = ratings.count()
    if rating_count > 0:
        rating_sum = sum([rating.value for rating in ratings])
        average_rating = rating_sum / rating_count
    else:
        average_rating = None
    return render(request, 'user_detail.html', {'user': user, 'average_rating': average_rating})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
