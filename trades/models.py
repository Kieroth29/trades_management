from django.db import models

class Trade(models.Model):
    code = models.CharField(max_length=255)
    execution_datetime = models.DateTimeField(auto_now_add=True)
    execution_price = models.FloatField()
