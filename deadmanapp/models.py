from __future__ import unicode_literals

from django.db import models

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.contact_name

class DeadmanSwitch(models.Model):
    name = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    interval = models.IntegerField(default=30)
    last_alive = models.DateTimeField()
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name
