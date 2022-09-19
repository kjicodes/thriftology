from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
SIZES= (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'X-Large')
 )

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    size = models.CharField(
        max_length=4,
        choices=SIZES,
        default=SIZES[0][0])
    condition = models.IntegerField()
    gender = models.CharField(max_length=1)
    isRental = models.BooleanField(default=False)
    date_sold = models.DateTimeField()
    date_listed = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='seller')
    buyer = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='buyer', null=True, default=None)


class Photo(models.Model):
    url = models.CharField(max_length=300)
    is_main_photo = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
