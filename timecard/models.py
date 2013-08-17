# -*- coding: utf-8 -*-

from django.db import models

class Timecard(models.Model):
    timecard_history = models.ManyToManyField(TimecardRecord)
    def get_total_hours():
        pass
    def add_record(self):
        pass
    def get_history(self):
        pass

class TimecardRecord(models.Model):
    arrive_time = models.DatetimeField(blank=True)
    leave_time = models.DatetimeField(blank=True)
