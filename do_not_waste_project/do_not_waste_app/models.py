from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    expire_date = models.DateField()
    remind_day = models.IntegerField()
    place = models.CharField(max_length=255)