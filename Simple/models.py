from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
