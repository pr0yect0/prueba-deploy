from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Quotes

class RegisterForms(UserCreationForm):
    first_name = forms.CharField(required=True,max_length=100)
    last_name = forms.CharField(required=True,max_length=100)
    username = forms.CharField(widget=forms.EmailInput, required=True,max_length=100)
    
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2']
        help_texts = {k:"" for k in fields}


class QuoteForm(forms.ModelForm):
    author = forms.CharField(min_length=3)
    quote = forms.CharField(widget=forms.Textarea,min_length=10)
    class Meta:
        model = Quotes
        fields = ['author','quote']

class UpdateUser(forms.ModelForm):
    username = forms.CharField(widget=forms.EmailInput, required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username']
        help_texts = {k:"" for k in fields}