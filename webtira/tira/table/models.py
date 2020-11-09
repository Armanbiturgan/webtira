
""" Model for test.
"""
from django.db import models


# Create your models here.
class np(models.Model):
    oblast = models.CharField(verbose_name="full name", max_length=100)
    region = models.CharField(verbose_name="full name", max_length=100)
    snp = models.CharField(verbose_name="full name", max_length=100)
    popul = models.CharField(verbose_name="full name", max_length=100)
    evdo = models.CharField(verbose_name="full name", max_length=100)
    adsl = models.CharField(verbose_name="full name", max_length=100)
    ftthb = models.CharField(verbose_name="full name", max_length=100)
    satellite = models.CharField(verbose_name="full name", max_length=100)
    twog = models.CharField(verbose_name="full name", max_length=100)
    threeg = models.CharField(verbose_name="full name", max_length=100)
    fourg = models.CharField(verbose_name="full name", max_length=100)
    vols = models.CharField(verbose_name="full name", max_length=100)
    lte = models.CharField(verbose_name="full name", max_length=100)
