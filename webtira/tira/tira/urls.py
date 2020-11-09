#!/usr/bin/env python
# coding: utf-8
from django.urls import include, path

import app.views


urlpatterns = [
    path('', app.views.base, name='base'),
    path('extensions/buttons/', app.views.buttons_extension, name='buttons_extension'),
    path('table/', include('table.urls')),
]
