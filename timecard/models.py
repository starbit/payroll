# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class TimecardRecord(models.Model):
    arrive_time = models.DateTimeField(blank=False)
    leave_time = models.DateTimeField(null=True)
    date = models.DateField(blank=False)
    user = models.ForeignKey(User)

    def work_time(self):
        return self.leave_time - self.arrive_time

    @property
    def work_hours(self):
        return int((self.work_time().total_seconds() + 1800) / 3600.0)


    @classmethod
    def find_or_create(cls, date):
        record = cls.objects.filter(date=date)

        if record:
            return record
        else:
            return cls()