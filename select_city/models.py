from datetime import datetime

from django.db import models


class Continents(models.Model):
    name = models.CharField(max_length=25)


class Countries(models.Model):
    continent = models.ForeignKey(Continents, on_delete=models.CASCADE, related_name="country")
    name = models.CharField(max_length=80)


class Cities(models.Model):
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=80)


class Plan(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    repeat = models.BooleanField(default=False)
    active = models.BooleanField()


