from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    account_user = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    class Meta:
        model= Account
        fields = [
            'account_user',
            'password',
            'email',
            ]
