from __future__ import unicode_literals

from django.db import models

class ContactNumber(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)

class DeadmanSwitch(models.Model):
    contact = models.ForeignKey(contact, on_delete=models.CASCADE)
    interval = models.IntegerField(default=30)
    last_alive = models.DateTimeField()
    disabled = models.BooleanField(default=false)
# Create your models here.
