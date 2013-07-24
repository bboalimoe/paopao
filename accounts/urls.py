from django.conf.urls import patterns, url
from accounts.views import *


urlpatterns = patterns('',
    url(r'^register/$', register),
)
