from django.conf.urls import patterns, include, url
from django.contrib import admin
from proxy import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'herokufreeproxy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('(?P<url>.*)', views.proxy_view),
)
