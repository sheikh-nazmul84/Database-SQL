from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    email = models.EmailField()
    contactNumber = models.CharField(max_length=20)

    class Meta:
        db_table="employee"