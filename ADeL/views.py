from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import  ContactForm
def home(request):
	return render(request,'pages/home.html')
def connexion(request):
	return render(request,'pages/connexion.html')

def register(request):    
	return render(request, 'pages/register.html')
