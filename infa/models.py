from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=30)

class uchet(models.Model):
    klient = models.CharField(max_length=30)
    agent = models.CharField(max_length=30)
    proc = models.CharField(max_length=100)
    addtime_date = models.DateTimeField()

