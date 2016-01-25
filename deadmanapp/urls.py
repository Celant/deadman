from django.conf.urls import url

from . import views

app_name = 'deadmanapp'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^switch/(?P<switch_id>[0-9]+)/$', views.switch_detail, name='switch-detail'),
    url(r'^switch/(?P<switch_id>[0-9]+)/answer/$', views.answer, name='answer'),
    url(r'^switch/(?P<switch_id>[0-9]+)/update/$', views.update, name='switch-update'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^account/$', views.user_account, name='account'),
    url(r'^account/password/$', views.user_password_change, name='password-change'),
]
