# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from payrollapp.models import Payroll
from timecard.models import Timecard
from payrollapp.models import PurchaseOrder

STATUS=(
        ('working','正常工作'),
        ('leave_of_absence','请假'),
        ('terminated','离职'),
        ('retired','退休'),

)
PAYMENT_METHOD=(
                ('mail','把支票邮寄到指定的地址'),
                ('transfer','转账到指定的银行账户'),
                ('pick','直接去公司财务处领取支票'),

                )

EMPLOYEE_TYPE=(
                ('hourly','钟点工'),
                ('salaried','全职员工'),
                ('commissioned','销售人员'),
    )

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    phone = models.CharField(max_length=11, null=True)
    name = models.CharField(max_length=20)
    # payroll = models.ForeignKey(Payroll)

    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    employee_status = models.CharField(max_length=20, choices=STATUS)
    hourly_salary = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    monthly_salary = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # purchase_order = models.ManyToManyField(PurchaseOrder)
    commission_rate = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    employee_type = models.CharField(max_length=15, choices=EMPLOYEE_TYPE, default='salaried')

    def is_pay_day(self):
        pass
    def get_bank_info(self):
        pass
    def get_pay_amount(self, pay_period):
        pass
    def calculate_pay(self):
        pass


    def __unicode__(self):
        return self.name


def create_user_profile(sender=None, instance=None, created=True, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class Leave(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(blank=False)

models.signals.post_save.connect(create_user_profile, sender=User)