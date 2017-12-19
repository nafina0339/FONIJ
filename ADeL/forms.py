from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

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
	def clean_username(self):
		user=self.cleaned_data['username']
		try:
			match = User.objects.get(username = user)

		except:
			return self.cleaned_data['username']
		raise forms.ValidationError("Ce nom d'utilisateur existe deja")
	def clean_email(self):
		email=self.cleaned_data['email']
		try:
			mt= validate_email(email)
		except :
			return forms.ValidationError("Cet format n'est pas correct")
		return email

	def clean_confirm_password(self):
		pas =self.cleaned_data['password']
		cpas=self.cleaned_data['confirm_password']
		MIN_LENGHT =8
		if pas and cpas:
			if pas != cpas:
				raise forms.ValidationError("Les mots de passe ne correspondent pas")
			else:
				if len(pas) < MIN_LENGHT:
					raise forms.ValidationError("Le mot de trop court minimum 8 caractère ")
				if pas.isdigit():
					raise forms.ValidationError("Le mot de passe ne doit pas etre que des numeric")


		
