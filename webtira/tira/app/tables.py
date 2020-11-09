#!/usr/bin/env python
# coding: utf-8
from datetime import date
import django

if django.VERSION >= (1, 10):
    from django.urls import reverse_lazy
else:
    from django.core.urlresolvers import reverse_lazy

from table.columns import Column
from table import Table
from table.utils import A
from app.models import Np


class ModelTable(Table):
    id = Column(field='id')
    oblast = Column(field='oblast')
    region  = Column(field='region')
    ruraldistrict = Column(field='ruraldistrict')
    snp = Column(field='snp')
    population = Column(field='population')
    gen2  = Column(field='gen2')
    gen3  = Column(field='gen3')
    gen4  = Column(field='gen4')
    ftth_b = Column(field='ftth_b')
    fo_plan = Column(field='fo_plan')
    project3g4g250 = Column(field='project3g4g250')
    radiomonitoring = Column(field='radiomonitoring')

    class Meta:
        model = Np


class ButtonsExtensionTable(Table):
    id = Column(field='id', header='KATO')
    oblast = Column(field='oblast', header='Область')
    region  = Column(field='region', header='Район')
    ruraldistrict = Column(field='ruraldistrict', header='Сельский Округ')
    snp = Column(field='snp', header='Нас. Пункт')
    population = Column(field='population', header='Население')
    gen2  = Column(field='gen2', header='2G')
    gen3  = Column(field='gen3', header='3G')
    gen4  = Column(field='gen4', header ='4G')
    ftth_b = Column(field='ftth_b', header ='FTTH/B (ВОЛС)')
    fo_plan = Column(field='fo_plan', header ='ВОЛС План')
    project3g4g250 = Column(field='project3g4g250', header ='Проект 3G/4G(250+)')
    radiomonitoring = Column(field='radiomonitoring', header ='Радиомониторинг (Дата:Примечание)')

    class Meta:
        model = Np
        template_name = 'buttons_table.html'
