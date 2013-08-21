# -*- coding: utf-8 -*-
from datetime import timedelta, date
from django.db import models
from django.contrib.auth.models import User
from payrollapp.models import Paycheck
from payrollapp.models import PurchaseOrder
from timecard.models import TimecardRecord

STATUS=(
        ('working',u'正常工作'),
        ('leave_of_absence',u'请假'),
        ('terminated',u'离职'),
        ('retired',u'退休'),

        )
PAYMENT_METHOD=(
                ('mail',u'把支票邮寄到指定的地址'),
                ('transfer',u'转账到指定的银行账户'),
                ('pick',u'直接去公司财务处领取支票'),

                )

EMPLOYEE_TYPE=(
                ('hourly',u'钟点工'),
                ('salaried',u'全职员工'),
                ('commissioned',u'销售人员'),
               )

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(u'手机号码', max_length=11, null=True)
    name = models.CharField(u'姓名', max_length=20)

    payment_method = models.CharField(u'工资支付方式', max_length=10, choices=PAYMENT_METHOD, default='pick')
    employee_status = models.CharField(u'员工状态', max_length=20, choices=STATUS, default='working')
    hourly_salary = models.DecimalField(u'小时工资', max_digits=6, decimal_places=2, default=0)
    monthly_salary = models.DecimalField(u'月工资', max_digits=8, decimal_places=2, default=0)
    commission_rate = models.DecimalField(u'业绩提成', max_digits=3, decimal_places=2, default=0)
    employee_type = models.CharField(u'员工类型', max_length=15, choices=EMPLOYEE_TYPE, default='salaried')
    bank_account = models.CharField(u'工资转帐银行账号', max_length=20, blank=True, null=True)
    mailing_address = models.CharField(u'工资支票邮寄地址', max_length=30, blank=True, null=True)

    def is_hourly(self):
        return self.employee_type == 'hourly'

    @property
    def employee_type_str(self):
        return filter(lambda x:x[0] == self.employee_type, EMPLOYEE_TYPE)[0][1]

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

class Leave(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField(blank=False)

def this_week_begin():
    today = date.today()
    return today - timedelta(days=today.weekday())

def this_month_begin():
    today = date.today()
    return date(today.year, today.month, 1)

def pay_all_hourly_employees():
    employees = User.objects.filter(userprofile__employee_type='hourly')
    for e in employees:
        date = this_week_begin()
        amount = 0
        while date <= date.today():
            if len(e.leave_set.filter(date=date).all()) != 0:
                continue
            try:
                timecard = e.timecardrecord_set.filter(date=date.today()).get()
                amount += timecard.work_hours * e.userprofile.hourly_salary
            except TimecardRecord.DoesNotExist:
                pass

            date += timedelta(days=1)
        e.paycheck_set.create(date=date, amount=amount)

def pay_all_salaried():
    employees = User.objects.filter(userprofile__employee_type='salaried')
    for e in employees:
        date = this_month_begin()
        levels = 0

        while date <= date.today():
            if len(e.leave_set.filter(date=date).all()) != 0:
                levels += 1
            date += timedelta(days=1)

        amount = float(e.userprofile.monthly_salary) / 30 * (30 - levels)
        e.paycheck_set.create(date=date, amount=amount)

def pay_all_commissioned():
    employees = User.objects.filter(userprofile__employee_type='commissioned')
    for e in employees:
        date = this_month_begin()
        levels = 0
        amount = 0

        while date <= date.today():
            if len(e.leave_set.filter(date=date).all()) != 0:
                levels += 1

            for p in e.purchaseorder_set.filter(time=date).all():
                amount += p.amount
            date += timedelta(days=1)

        amount = float(e.userprofile.monthly_salary) / 30 * (30 - levels) + float(amount * e.userprofile.commission_rate)
        e.paycheck_set.create(date=date, amount=amount)
