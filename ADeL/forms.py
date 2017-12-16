from django import forms
from .models import *
from django.contrib.auth.models import User

class userform(forms.ModelForm):
	username= forms.CharField(widget=forms.TextInput(
		attrs={'class' :'form-control', 'placeholder':'Username'}
		), required=True, max_length=50)
	email= forms.CharField(widget=forms.EmailInput(
		attrs={'class' :'form-control', 'placeholder':'Email'}
		), required=True, max_length=50)
	first_name= forms.CharField(widget=forms.TextInput(
		attrs={'class' :'form-control', 'placeholder':'Prenom'}
		), required=True, max_length=50)
	last_name= forms.CharField(widget=forms.TextInput(
		attrs={'class' :'form-control', 'placeholder':'Nom'}
		), required=True, max_length=50)
	password= forms.CharField(widget=forms.PasswordInput(
		attrs={'class' :'form-control', 'placeholder':'Mot de passe'}
		), required=True, max_length=50)
	confirm_password= forms.CharField(widget=forms.PasswordInput(
		attrs={'class' :'form-control', 'placeholder':'Confirmation'}
		), required=True, max_length=50)
	class Meta():
		model=User
		fields = ['username', 'email', 'first_name', 'last_name', 'password']
