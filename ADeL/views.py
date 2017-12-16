from django.shortcuts import render
from django.http import *
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
def home(request):
	return render(request,'pages/home.html')
def connexion(request):
	if request.method == "POST":
		username =request.POST['user']
		password =request.POST['pas']
		try:
			user= auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return render(request, 'pages/welcome.html')
			else:
				messages.error(request,'username ou password incorrect')
		except auth.ObjectNotExist:
			print("user invalid")

	return render(request,'pages/connexion.html')

def register(request): 
	if request.method == 'POST':
		form1=userform(request.POST) 
		if form1.is_valid():
				username = form1.cleaned_data['username']
				email = form1.cleaned_data['email']
				first_name = form1.cleaned_data['first_name']    
				last_name = form1.cleaned_data['last_name']  
				password = form1.cleaned_data['password']  
				confirm_password = form1.cleaned_data['confirm_password'] 
				User.objects.create_user(username = username, email = email, first_name = first_name, last_name = last_name, password = password) 
				messages.success(request, 'Utilisateur enregistrer avec succès')
				return HttpResponseRedirect('/register/')
	else:
		form1 = userform()
	return render(request, 'pages/register.html', {'frm':form1})
