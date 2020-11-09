from django.db import models


class Np(models.Model):
    oblast = models.CharField(verbose_name="full name", max_length=100)
    region = models.CharField(verbose_name="full name", max_length=100)
    ruraldistrict = models.CharField(verbose_name="full name", max_length=100)
    snp = models.CharField(verbose_name="full name", max_length=100)
    population = models.CharField(verbose_name="full name", max_length=100)
    gen2 = models.CharField(verbose_name="full name", max_length=100)
    gen3 = models.CharField(verbose_name="full name", max_length=100)
    gen4 = models.CharField(verbose_name="full name", max_length=100)
    ftth_b = models.CharField(verbose_name="full name", max_length=100)
    fo_plan = models.CharField(verbose_name="full name", max_length=100)
    project3g4g250 = models.CharField(verbose_name="full name", max_length=100)
    radiomonitoring = models.CharField(verbose_name="full name", max_length=100)

    class Meta:
        db_table = 'np'
