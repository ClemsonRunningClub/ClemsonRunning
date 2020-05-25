from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#creating a class using the UserCreationForm built into django
#model=User indicates this will impact the User model imported from the User model build
class AccountForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "username", "password1", "password2"]
