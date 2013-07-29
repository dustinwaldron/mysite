from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

from resume.models import *

def resume_page(request):
	skills = {}
	skillCategories = list(SkillCategory.objects.all())
	for cat in skillCategories:
		skills[cat] = [];
		temp = list(Skill.objects.filter(category = cat))
		for s in temp:
			skills[cat].append(s)

	classes = list(Course.objects.all())
	experiences = list(Experience.objects.all())
	accomplishments = list(Accomplishment.objects.all())
	context = { 'classes':classes, 'experiences':experiences, 'skills':skills, 'accomplishments':accomplishments}
	return render(request, 'resume_page.html',context)