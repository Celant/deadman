from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deadman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('deadmanapp.urls')),
    url(r'^admin/', admin.site.urls),
)
