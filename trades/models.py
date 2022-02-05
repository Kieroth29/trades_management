from django.db import models

class Trade(models.Model):
    code = models.CharField()
    execution_datetime = models.DateTimeField(auto_now_add=True)
    execution_price = models.FloatField()
