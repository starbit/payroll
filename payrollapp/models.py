# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

class Payroll(models.Model):
    user = models.ForeignKey(User)
    def generate_paychecks():
        pass


class Paycheck(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)


class PurchaseOrder(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=200)
    time = models.DateTimeField(blank=False)


class PayPeriod(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
