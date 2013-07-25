from django.conf.urls import patterns, url
from accounts.views import *


urlpatterns = patterns('',
    url(r'^register/$', register),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_user),
)
