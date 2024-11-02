from django.db import models

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    population = models.IntegerField()
