from django import forms
from deadmanapp.models import Contact, DeadmanSwitch, CONTACT_TYPES

class DeadmanSwitchForm(forms.Form):
    name = forms.CharField(max_length=50)
    contact = forms.ModelChoiceField(queryset=Contact.objects.all())
    interval = forms.IntegerField()
    disabled = forms.BooleanField()

class ContactForm(forms.Form):
    contact_name = forms.CharField(max_length=50)
    contact_info = forms.CharField(max_length=50)
    contact_type = forms.CharField(max_length=50, widget=forms.Select(choices=CONTACT_TYPES))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
