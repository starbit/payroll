# -*- coding: utf-8 -*-
from django_cron import CronJobBase, Schedule
from django.db import models
from django.contrib.auth.models import User
from payrollapp.models import Paycheck
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
    
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD)
    employee_status = models.CharField(max_length=20, choices=STATUS)
    hourly_salary = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    monthly_salary = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    commission_rate = models.DecimalField(max_digits=3, decimal_places=3, default=0)
    employee_type = models.CharField(max_length=15, choices=EMPLOYEE_TYPE, default='salaried')
    bank_account = models.CharField(max_length=20, blank=True)
    mailing_address = models.CharField(max_length=30, blank=True)

    def get_pay_year_to_date(self):#从年初到今天的工资 其实就是把这段时间所有的paycheck的amount加起来
        pass
    
    def generate_paycheck(self):#定期每个工作周期生成工资支票 某周五或每月最后一个工作日
        pass
    
    def get_total_hours_worked(self, start_date, end_date):#从一个日期到另一个日期工作小时总数
        pass
    
    def get_leave_report(self, start_date, end_date):#从一个日期到另一个日期所有的请假记录
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



#下面的还没写好
class PayHourlyEmployee(CronJobBase):
    RUN_EVERY_MINS = 120 # ever
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code
    
    def do(self):
        pass    # do your thing here

class PaySalariedEmployee(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hour
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code
    
    def do(self):
        pass    # do your thing here
