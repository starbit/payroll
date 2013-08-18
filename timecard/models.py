# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class TimecardRecord(models.Model):
    arrive_time = models.DateTimeField(blank=False)
    leave_time = models.DateTimeField(null=True)
    date = models.DateField(blank=False)
    user = models.ForeignKey(User)

    @classmethod
    def find_or_create(cls, date):
        record = cls.objects.filter(date=date)

        if record:
            return record
        else:
            return cls()




class Timecard(models.Model):
    timecard_history = models.ManyToManyField(TimecardRecord)
    def get_total_hours():
        pass
    def add_record(self):
        pass
    def get_history(self):
        pass