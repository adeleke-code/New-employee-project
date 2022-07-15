from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=250)
    salary = models.FloatField()
    linkedin = models.URLField()
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="sub_ordinate")
    department = models.CharField(max_length=350)
    employee_num = models.CharField(max_length=6, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name

class Branch(models.Model):
    branch_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE,
    related_name="second_option")
    branch_id = models.CharField(max_length=350, null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name