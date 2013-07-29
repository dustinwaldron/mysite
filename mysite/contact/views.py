from django.http import HttpResponse
from django.shortcuts import render

from contact.form import *

def contact_form(request):
    if request.method == 'POST':
    	form = ContactForm(request.POST)
    	if form.is_valid():
    		name = form.cleaned_data['name']
    		email = form.cleaned_data['email']
    		organization = form.cleaned_data['organization']
    		message = form.cleaned_data['message']
    		recipient = ['junk@junk.com']
    		'''from django.core.mail import send_mail
    		subject = str(organization) + " has contacted you"
    		send_mail(subject, message, email, recipient)'''
    		return HttpResponseRedirect('/contact/confirmation/')
    else:
    	form = ContactForm()

    return render(request,"contact_form.html",{ 'form':form, })

def confirmation(request):
	return render(request, "confirm.html")