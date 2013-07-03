from django.http import HttpResponse
from django.shortcuts import render

from Profile.models import *

def profile_page(request):
	return render(request, 'profile_page.html')