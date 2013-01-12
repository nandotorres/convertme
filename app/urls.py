# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('app.views',
    url(r'^upload/$', 'upload', name='upload'),
    url(r'^notify/([0-9]{1,})$', 'notify', name='notify'),
    (r"^$", direct_to_template, {"template": "index.html"})
)