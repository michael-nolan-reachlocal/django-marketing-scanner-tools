from django.db import models

# Create your models here.

# We need:
# Person's data
# Website data
# Marketo submission

# Classes
# Contact: What we send to Marketo
# WebData: Used to generate SEO report
# Algo: SEO algorithms: used to generate WebData

class Algo(models.Model):
  algo_description = models.CharField(max_length=500)
  algo_file = models.CharField(max_length=50)

class WebData(models.Model):
  algo = models.ForeignKey(Algo)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

class Report(models.Model):
  data = models.ForeignKey(WebData)

class Contact(models.Model):
  algos = models.ForeignKey(Algo)
  report = models.ForeignKey(Report)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  company_name = models.CharField(max_length=50)
  contact_email = models.CharField(max_length=50)
  contact_phone = models.CharField(max_length=50)
  
  submit_date = models.DateTimeField('date published')
