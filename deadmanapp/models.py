from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class ContactType(models.Model):
    name = models.CharField(max_length=50, default="New ContactType")

    def __str__(self):
        return self.name

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=50)
    contact_type = models.ForeignKey(ContactType, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.contact_name

class DeadmanSwitch(models.Model):
    name = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT)
    interval = models.IntegerField(default=30)
    last_alive = models.DateTimeField()
    disabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class DeadmanSwitchForm(ModelForm):
    class Meta:
        model = DeadmanSwitch
        fields = ['name', 'contact', 'interval', 'disabled']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = []
