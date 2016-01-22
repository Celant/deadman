from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader, RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from deadmanapp.forms import DeadmanSwitchForm, LoginForm

from .models import DeadmanSwitch

@login_required
def index(request):
    switch_list = DeadmanSwitch.objects.order_by('id')
    return render(request, 'deadmanapp/index.html', {'switch_list': switch_list})

@login_required
def switch_detail(request, switch_id):
    switch = get_object_or_404(DeadmanSwitch, pk=switch_id)
    data = {'name' : switch.name, 'interval' : switch.interval, 'contact' : switch.contact, 'disabled' : switch.disabled}
    form = DeadmanSwitchForm(initial=data)
    return render(request, 'deadmanapp/switch_detail.html', {'form': form, 'switch': switch})

@login_required
def contacts(request, switch_id):
    contact_list = Contacts.objects.order_by('contact_name')
    return render(request, 'deadmanapp/contacts.html', {'contact_list': contact_list})

@login_required
def update(request, switch_id):
    switch = get_object_or_404(DeadmanSwitch, pk=switch_id)
    switch.name = request.POST.get('name', "Default Switch")
    switch.interval = request.POST.get('interval', 30)
    if 'disabled' in request.POST:
        switch.disabled = True
    else:
        switch.disabled = False
    switch.save()

    return HttpResponseRedirect(reverse('deadmanapp:index'))

def answer(request, switch_id):
    return HttpResponse("You're responding to switch {0}.".format(switch_id))

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/app/')
            else:
                # An inactive account was used - no logging in!
                return redirect(reverse('deadmanapp:login') + '?disabled=true')
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details"
            return redirect(reverse('deadmanapp:login') + '?failed=true')

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        form = LoginForm()

        if 'failed' in request.GET:
            error_message = 'Incorrect username/password combination.'
            return render(request, 'deadmanapp/login.html', {'form': form, 'error_message': error_message})
        if 'disabled' in request.GET:
            error_message = 'Your account is disabled.'
            return render(request, 'deadmanapp/login.html', {'form': form, 'error_message': error_message})
        if 'logout' in request.GET:
            success_message = 'You have been succesfully logged out'
            return render(request, 'deadmanapp/login.html', {'form': form, 'success_message': success_message})

        return render(request, 'deadmanapp/login.html', {'form': form})

@login_required
def user_logout(request):

    logout(request)

    return redirect(reverse('deadmanapp:login') + '?logout=true')
