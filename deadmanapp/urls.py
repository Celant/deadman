from django.conf.urls import url

from . import views

app_name = 'deadmanapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<switch_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<switch_id>[0-9]+)/answer/$', views.answer, name='answer'),
    url(r'^(?P<switch_id>[0-9]+)/update/$', views.update, name='update'),
]
