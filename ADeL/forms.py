from django import forms
from .models import *
from django.contrib.auth.models import User

class userform(forms.ModelForm):
	nom= forms.CharField(widget=forms.TextInput(
		attrs={'class' :'form-control', 'placeholder':'Nom'}
		), required=True, max_length=50)
	prenom= forms.CharField(widget=forms.TextInput(
		attrs={'class' :'form-control', 'placeholder':'Prénom'}
		), required=True, max_length=50)
	pseudo= forms.CharField(widget=forms.TextInput(
		attrs={'class' :'form-control', 'placeholder':'Pseudo'}
		), required=True, max_length=50)
	email= forms.CharField(widget=forms.EmailInput(
		attrs={'class' :'form-control', 'placeholder':'Adresse Email'}
		), required=True, max_length=50)
	password= forms.CharField(widget=forms.PasswordInput(
		attrs={'class' :'form-control', 'placeholder':'Mot de passe'}
		), required=True, max_length=50)
	password1= forms.CharField(widget=forms.PasswordInput(
		attrs={'class' :'form-control', 'placeholder':'Confirmation'}
		), required=True, max_length=50)
	class Meta():
		model=User
		fields = ['nom', 'prenom', 'pseudo', 'email', 'password']
