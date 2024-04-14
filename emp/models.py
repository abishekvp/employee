from django.db import models

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_code = models.CharField(max_length=10, unique=True)
    emp_name = models.CharField(max_length=100)
    emp_age = models.IntegerField()

