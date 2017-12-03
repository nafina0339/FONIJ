from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import  ContactForm
def home(request):
	return render(request,'pages/home.html')
def about(request):
	return render(request,'pages/about.html')

def contact(request):    
	 if request.method == 'POST':  
		 form = ContactForm(request.POST)  
			   # Nous reprenons les données        
		 if form.is_valid(): 
				   # Nous vérifions que les données envoyées sont valides          
				     # Ici nous pouvons traiter les données du formulaire          
				       sujet = form.cleaned_data['sujet']           
				       message = form.cleaned_data['message']         
				       envoyeur = form.cleaned_data['envoyeur']          
				       renvoi = form.cleaned_data['renvoi']          
				               # Nous pourrions ici envoyer l'e-mail grâce aux données que nous venons de récupérer         
				       envoi = True   
     
	 			      
	 else: 
	                  # Si ce n'est pas du POST, c'est probablement une requête GET  
	       form = ContactForm() 
	                         # Nous créons un formulaire vide 
	
	 return render(request, 'pages/name.html', locals())
