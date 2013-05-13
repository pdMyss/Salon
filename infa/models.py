from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=30)

class People(models.Model):
    fam = models.CharField(max_length=30)
    im = models.CharField(max_length=30)
    otv = models.CharField(max_length=30)