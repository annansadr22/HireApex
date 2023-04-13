from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('<int:user_id>/rate/', views.rate_user, name='rate_user'),
]
