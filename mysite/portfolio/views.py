from django.http import HttpResponse
from django.shortcuts import render

from portfolio.models import *

def portfolio_page(request):
	all_projects = list(Project.objects.all())
	all_pictures = list(ProjectImage.objects.all())
	all_projects = zip(all_pictures, all_projects)
	context = { 'all_projects': all_projects, 'all_pictures':all_pictures } #'all_pictures':all_pictures 
	return render(request, 'portfolio_page.html',context)