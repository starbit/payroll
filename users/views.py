# -*- coding: utf-8 -*-

from datetime import datetime, date
from django import forms
from django.template.response import TemplateResponse
from payroll.settings import DEFAULT_FROM_EMAIL
# from django.db.transaction import commit_on_success
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
from django.contrib.auth import login, authenticate,logout
from .forms import ResetPasswordForm, ChangePasswordForm
from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect, render_to_response, HttpResponse,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext,Template, Context

from timecard.models import TimecardRecord
from payrollapp.forms import PurchaseOrderForm


@login_required
def user(request):
    user = request.user
    try:
        timecardrecord = user.timecardrecord_set.filter(date=date.today()).get()
        if timecardrecord and timecardrecord.leave_time:
            work_done = True
            work_time = timecardrecord.leave_time - timecardrecord.arrive_time
    except TimecardRecord.DoesNotExist:
        pass

    return render_to_response('users/user.html', locals())

@login_required
def arrive(request):
    user = request.user
    arrive_time = datetime.now()
    timecardrecord_date = date.today()
    user.timecardrecord_set.create(arrive_time=arrive_time, date=timecardrecord_date)
    return redirect('/user')


@login_required
def leave(request):
    user = request.user
    timecardrecord = user.timecardrecord_set.filter(date=date.today(), leave_time__isnull=True).get()
    timecardrecord.leave_time = datetime.now()
    timecardrecord.save()
    return redirect('/user')


def reset_psw(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(domain_override=request.get_host(), from_email=DEFAULT_FROM_EMAIL, email_template_name="users/password_reset_email.html")
            return render_to_response('users/reset_psw_sended.html', {})
        else:
            return TemplateResponse(request, 'users/reset_psw.html', {'form': form})
    form = PasswordResetForm()
    return TemplateResponse(request, 'users/reset_psw.html', {'form': form})



def reset_psw_confirm(request, uid, token):
    from django.utils.http import base36_to_int
    user = User.objects.get(pk = base36_to_int(uid))

    if request.method == 'POST':
        form = ResetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('users/reset_psw_done.html', {})
        else:
            return TemplateResponse(request, 'users/reset_psw_confirm.html', {'form': form})
    form = ResetPasswordForm(user)
    return TemplateResponse(request, 'users/reset_psw_confirm.html', {'form': form})


def _set_psw(request):
    if request.method == 'POST':
        form = ChangePasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            return render_to_response('users/change_psw_done.html', {})
        else:
            return TemplateResponse(request, 'users/setting_psw.html', {'form': form})
    form = ChangePasswordForm(user = request.user)
    return TemplateResponse(request, 'users/setting_psw.html', {'form': form})



def server_error(request, template_name='500.html'):
    r = render_to_response(template_name,
                           context_instance = RequestContext(request)
                           )
    r.status_code = 500
    return r

def server_error_404(request, template_name='404.html'):
    r =  render_to_response(template_name,
                            context_instance = RequestContext(request)
                            )
    r.status_code = 404
    return r
