from django_cron import CronJobBase, Schedule

class PayHourlyEmployee(CronJobBase):
    RUN_EVERY_MINS = 1 # ever

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'users.pay_hourly_employee'    # a unique code

    def do(self):
        print "sdfsdf"
