from django.db import models
from accounts.models import User
# Create your models here.

class Merchant(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length=12, unique=True)
    location = models.CharField(max_length=255)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    