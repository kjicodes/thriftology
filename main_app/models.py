from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'X-Large')
)

GENDER = (
    ('F', 'FEMALE'),
    ('M', 'MALE'),
    ('U', 'UNISEX')
)

class Listing(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    price = price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(
        max_length=3,
        choices=SIZES,
        default=SIZES[0][0]
    )
    condition = models.IntegerField()
    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default=GENDER[0][0]
        )
    isRental = models.BooleanField(default=False)
    date_sold = models.DateTimeField(null=True, default=None)
    date_listed = models.DateTimeField(default=timezone.now)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE)
    buyer = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name='buyer', null=True, default=None)

    def __str__(self):
        return f"{self.title}  - seller:{self.seller} buyer:{self.buyer}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'listing_id': self.id})


class Photo(models.Model):
    url = models.CharField(max_length=300)
    is_main_photo = models.BooleanField(default=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
