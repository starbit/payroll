# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

class Paycheck(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    user = models.ForeignKey(User)
    date = models.DateField(blank=False)
    def __unicode__(self):
        return self.user.username + " " + str(self.amount) + u'元' + " " + str(self.date)




class PurchaseOrder(models.Model):
    user = models.ForeignKey(User)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=200)
    time = models.DateField(blank=False)
    def __unicode__(self):
        return self.user.username + " "+ str(self.amount) + u'元'

