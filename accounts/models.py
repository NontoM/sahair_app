from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    is_customer = models.BooleanField(default=False)
    is_merchant = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_image', null=True, blank=True)

    def __str__(self):
        return self.user.username
