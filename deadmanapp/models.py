from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

CONTACT_TYPES = (
    ('PHONE', 'Phone Number'),
    ('EMAIL', 'Email Address'),
)

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_info = models.CharField(max_length=50)
    contact_type = models.CharField(max_length=50, choices=CONTACT_TYPES)

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

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password_expired = models.BooleanField(verbose_name="Must change password on next login", default=False)

class DeadmanSwitchForm(ModelForm):
    class Meta:
        model = DeadmanSwitch
        fields = ['name', 'contact', 'interval', 'disabled']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_info', 'contact_type']
