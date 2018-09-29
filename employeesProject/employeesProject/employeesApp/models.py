from django.db import models

class Type(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)

class Employee(models.Model):
	firstname = models.CharField(max_length=100)
	surname = models.CharField(max_length=100)
	email = models.CharField(max_length=100, unique=True)
	password = models.CharField(max_length=100)
	employeeType = models.ForeignKey(Type, on_delete=models.CASCADE)



