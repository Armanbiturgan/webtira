#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render

from table.views import FeedDataView

from app.tables import (
    ModelTable,
    ButtonsExtensionTable
)

def base(request):
    table = ModelTable()
    return render(request, "index.html", {'people': table})

def buttons_extension(request):
    table = ButtonsExtensionTable()
    return render(request, "index.html", {'people': table})
