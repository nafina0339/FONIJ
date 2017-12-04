from django.shortcuts import render
from django.http import *
from .forms import *
from .models import *
from django.contrib.auth.models import User
def home(request):
	return render(request,'pages/home.html')
def connexion(request):
	return render(request,'pages/connexion.html')

def register(request): 
	if request.method == 'POST':
		form1=userform(request.POST) 
		if form1.is_valid():
				nom = form1.cleaned_data['nom']
				prenom = form1.cleaned_data['prenom']
				pseudo = form1.cleaned_data['pseudo']    
				email = form1.cleaned_data['email']  
				password = form1.cleaned_data['password']  
				password1 = form1.cleaned_data['password1'] 
				User.objects.create_user(nom = nom, prenom = prenom, pseudo = pseudo, email = email, password = password) 
				return HttpResponseRedirect('/register/')
	else:
		form1 = userform()
	return render(request, 'pages/register.html', {'frm':form1})
