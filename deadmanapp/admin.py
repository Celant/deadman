from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from deadmanapp.models import Contact, DeadmanSwitch, UserDetails

# Register your models here.
class UserDetailsInLine(admin.StackedInline):
    model = UserDetails
    can_delete = False
    verbose_name_plural = 'user details'

class UserAdmin(BaseUserAdmin):
    inlines = (UserDetailsInLine, )

admin.site.register(Contact)
admin.site.register(DeadmanSwitch)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
