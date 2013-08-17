# -*- coding: utf-8 -*-

from django.db import models

class Payroll(models.Model):
    def generate_paychecks():
        pass

class Paycheck(models.Model):
    amount = models.FloatField(max_digits=8, decimal_places=2, default=0)

class PurchaseOrder(models.Model):
    amount = models.FloatField(max_digits=10, decimal_places=2, default=0)



class PayPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
