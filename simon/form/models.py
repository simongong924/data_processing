from django.db import models

# Create your models here.
class Job(models.Model):
	name = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	job_number = models.CharField(max_length=200)
	quantity = models.IntegerField(default=0)
	data = models.IntegerField(default=0)
	def __unicode__(self):
		output = "Job Number: "+self.job_number+"\n"
		output += "Name: "+self.name+"\n"
		output += "Company: "+self.company+"\n"
		output += "Data: "+str(self.data)
		return output