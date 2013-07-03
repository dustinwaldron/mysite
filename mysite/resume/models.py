from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=50,)
    number = models.CharField(max_length=10)
    description = models.TextField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __unicode__(self):
    	return self.number

    class Meta:
    	ordering = ['number']

class Skill(models.Model):
    name = models.CharField(max_length=50)


    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class SkillCategory(models.Model):
    name = models.CharField(max_length=200)
    position = models.PositiveIntegerField()
    skills = models.ManyToManyField('Skill')

    class Meta:
        ordering = ["position"]

    def __unicode__(self):
        return self.name

class Experience(models.Model):
	title = models.CharField(max_length=50)
	primary_location = models.CharField(max_length=50)
	secondary_location = models.CharField(max_length=25)
	description = models.TextField()
	end_date = models.DateField(blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)

	class Meta:
		ordering = ['start_date']

	def __unicode__(self):
		return self.title
