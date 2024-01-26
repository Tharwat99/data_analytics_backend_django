from django.db import models

class Data(models.Model):
    month = models.CharField(max_length= 100, unique = True)
    revenue = models.DecimalField(decimal_places= 2, max_digits=10)
    expenses = models.DecimalField(decimal_places= 2, max_digits=10)
    profit = models.DecimalField(decimal_places= 2, max_digits=10)