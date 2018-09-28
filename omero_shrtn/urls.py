#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns

from . import views


urlpatterns = patterns(
    'django.views.generic.simple',

    # Expand a shortened link
    url(r'^(?P<u>.+)$', views.unshrtn, name="unshrtn"),
)
