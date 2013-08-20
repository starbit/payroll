from django_cron import CronJobBase, Schedule

class PayHourlyEmployee(CronJobBase):
    RUN_EVERY_MINS = 1 # ever
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'users.pay_hourly_employee'    # a unique code
    
    def do(self):
        print 'pay_hourly'    # do your thing here
'''
    class PaySalariedEmployee(CronJobBase):
    RUN_EVERY_MINS = 2 # every 2 hour
    
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'users.pay_salaried_employee'    # a unique code
    
    def do(self):
    user = User.objects.get(id=1)
    userprofile = user.get_profile()
    userprofile.phone = '8888888'
    userprofile.save()
    fh = open('/Users/aoli/code/payroll/test', 'a')
    fh.write('1')
    fh.close()
    print 'pay_salaried'   # do your thing here
    '''