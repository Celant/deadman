from django.contrib import admin

from .models import Contact, ContactType, DeadmanSwitch

admin.site.register(Contact)
admin.site.register(DeadmanSwitch)
admin.site.register(ContactType)

# Register your models here.
