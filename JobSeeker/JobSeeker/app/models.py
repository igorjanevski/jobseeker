"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Country(models.Model):    
    name = models.CharField(max_length = 50)
    active = models.BooleanField(default = True)
    date_inserted = models.DateField()

class City(models.Model):
    name = models.CharField(max_length = 50)
    country = models.ForeignKey(Country)
    active = models.BooleanField(default = True)
    date_inserted = models.DateField()

class Industry(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    active = models.BooleanField(default = True)
    date_inserted = models.DateField()

class Jobs(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    industry = models.ForeignKey(Industry)
    active = models.BooleanField(default = True)
    date_inserted = models.DateField()

class Employeers(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 64)
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    active = models.BooleanField(default = True)
    date_inserted = models.DateField()

class Candidates(models.Model):
    name = models.CharField(max_length = 100)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 64)
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    active = models.BooleanField(default = True)
    date_inserted = models.DateField()
    cv = models.BinaryField()