from django import forms
from .models import User
class RegisterUserForm(forms.ModelForm):
	password= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))
	password2= forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}))

	class Meta:
		model =User

		fields= ['username', 'email']

		widgets = {
		'username':forms.TextInput(attrs={'class':'input'}),
		'email':forms.EmailInput(attrs={'class':'input'}),
		}