from django.db import models

# Create your models here.

from datetime import datetime, timedelta
from cinema_ebooking_system import constants
from core.models import TimeStamp


class Movie(TimeStamp):
   title = models.CharField(max_length=255)
   alias = models.CharField(max_length=255, blank=True, null=True)
   movie_code = models.CharField(max_length=255, blank=True, null=True)
   expire_date = models.DateTimeField(null=True, blank=True)
   poster_image = models.FileField(upload_to="images/", null=True)

class Show(TimeStamp):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    seat_row = models.CharField(max_length=10, blank=True, null=True)
    amount = models.FloatField(default=0)


class Promotion(TimeStamp):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=True, null=True)
    promo_code = models.CharField(max_length=100, null=True, blank=True)
    off_amount = models.FloatField(default=0)
    off_percent = models.FloatField(default=0)
    promo_type = models.CharField(max_length=100, choices=constants.COUPON_TYPES, default="percent")
    min_amount = models.FloatField(default=0)





    



   

