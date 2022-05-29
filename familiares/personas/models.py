from django.db import models

class Personas(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    documento = models.IntegerField()
    fechanacimiento = models.DateField()
    parentesco = models.CharField(max_length=30)