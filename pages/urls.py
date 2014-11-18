# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'pages.views',

    url(r'^pages/$', 'pages', name='pages_pages'),
    url(r'^page/(?P<slug>[-\w]+)/$', 'page', name='pages_page'),
)
