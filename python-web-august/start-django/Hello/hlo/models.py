from django.db import models

# Create your models here.

class ContactU(models.Model):
    Name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    Email = models.CharField(max_length=50)
    message = models.TextField()