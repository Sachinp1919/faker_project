from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=30)
