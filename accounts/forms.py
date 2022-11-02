from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User

class CustomerSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name','email', 'username', 'password1', 'password2')
