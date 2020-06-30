from django.db import models
from multiselectfield import MultiSelectField
import datetime
# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=30)
    address = models.TextField()
    phone = models.IntegerField()
    time =models.DateTimeField()
    orders = models.TextField(max_length=2000)
    guests = models.IntegerField()
    password = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Customer details"
    def __str__(self):
        return self.name