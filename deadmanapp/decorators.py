from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

def password_expired(function):
    def wrapper(request, *args, **kw):
        user=request.user
        if not (user.id and user.userdetails.password_expired == False):
            return redirect(reverse('deadmanapp:password-change'))
        else:
            return function(request, *args, **kw)
    return wrapper
