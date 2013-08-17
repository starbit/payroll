# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

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



class UserProfile(models.Model):
    user = models.ForeignKey(User)
    phone = models.CharField(max_length=11, null=True)
    name = models.CharField(max_length=20)
    payroll = models.ForeignKey(Payroll)
    timecard = models.ForeignKey(Timecard)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    
    employee_status = models.CharField(max_length=20, choices=STATUS)
    
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
    
    class Meta:
        abstract = True


class HourlyEmployee(UserProfile):
    hourly_salary = models.FloatField(max_digits=6, decimal_places=2)
    def change_to_salaried():
        pass
    def change_to_commissioned():
        pass
    



class SalariedEmployee(UserProfile):
    monthly_salary = models.FloatField(max_digits=8, decimal_places=2)
    def change_to_commissioned():
        pass
    def change_to_hourly():
        pass
    


class CommissionedEmployee(SalariedEmployee):
    purchase_order = models.ManyToManyField(PurchaseOrder)
    commission_rate = models.FloatField(max_digits=3, decimal_places=3)
    def change_to_hourly():
        pass
    def change_to_salaried():
        pass



def create_user_profile(sender=None, instance=None, created=True, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

models.signals.post_save.connect(create_user_profile, sender=User)


