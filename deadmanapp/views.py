from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import loader

from .models import DeadmanSwitch

def index(request):
    switch_list = DeadmanSwitch.objects.order_by('id')
    return render(request, 'deadmanapp/index.html', {'switch_list': switch_list})

def detail(request, switch_id):
    switch = get_object_or_404(DeadmanSwitch, pk=switch_id)
    return render(request, 'deadmanapp/detail.html', {'switch': switch})

def answer(request, switch_id):
    return HttpResponse("You're responding to switch {0}.".format(switch_id))

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
