#!/usr/bin/env python
# coding: utf-8
from django.urls import path

from table.views import FeedDataView


urlpatterns = [
    path('ajax/(?P<token>\w{32})/', FeedDataView.as_view(), name='feed_data'),
]
