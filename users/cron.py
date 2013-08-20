from django_cron import CronJobBase, Schedule
from users.models import pay_all_hourly_employees, pay_all_salaried, pay_all_commissioned

class PayHourlyEmployee(CronJobBase):
    RUN_EVERY_MINS = 1 # ever

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'users.pay_hourly_employee'    # a unique code

    def do(self):
        pay_all_hourly_employees()
        pay_all_salaried()
        pay_all_commissioned()
