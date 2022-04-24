import email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from user_accounts.models import FileModel

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username", "email", "password1", "password2")


# File verification and upload form
class fileForm(forms.Form):
    name=forms.CharField(max_length=60)
    file=forms.FileField()
    class Meta:
        model=FileModel
        fields='__all__'
