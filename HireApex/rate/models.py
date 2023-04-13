from django.db import models
from django.contrib.auth.models import User

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_received')
    value = models.IntegerField(choices=((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')))
    rater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_given')
