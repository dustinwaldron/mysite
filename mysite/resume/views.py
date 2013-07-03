from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

from resume.models import *

def resume_page(request):
	classes = list(Course.objects.all())
	experiences = list(Experience.objects.all())
	context = { 'classes':classes, 'experiences':experiences }
	return render(request, 'resume_page.html',context)