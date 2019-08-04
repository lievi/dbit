from django.db import models


class Expenses(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    value = models.FloatField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
