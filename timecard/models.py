# -*- coding: utf-8 -*-

from django.db import models


class TimecardRecord(models.Model):
    arrive_time = models.DateTimeField(blank=True)
    leave_time = models.DateTimeField(blank=True)


class Timecard(models.Model):
    timecard_history = models.ManyToManyField(TimecardRecord)
    def get_total_hours():
        pass
    def add_record(self):
        pass
    def get_history(self):
        pass