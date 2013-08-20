from django.conf.urls import patterns, include, url
from users.forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from payrollapp.views import PurchaseOrderCreate, PurchaseOrderUpdate, PurchasesView, PurchaseOrderDelete

from users.views import LeavesView, LeaveCreate, PayView, TimeView

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^user/$', 'users.views.user', name='user'),
    url(r'^user/leaves$', login_required(LeavesView.as_view()), name='user_leaves'),
    url(r'^user/ask_leave$', login_required(LeaveCreate.as_view()), name='ask_leave'),

    url(r'^user/pays$', login_required(PayView.as_view()), name='pays'),
    url(r'^user/times$', login_required(TimeView.as_view()), name='times'),


    url(r'^user/arrive$', 'users.views.arrive', name='user_arrive'),
    url(r'^user/leave$', 'users.views.leave', name='user_leave'),
    url(r'^user/settings/(?P<item>\w*)$', 'users.views.settings', name='user_settings'),
    url(r'^contact/$', 'users.views.contact',name='contact'),
    url(r'^thanks/$', 'users.views.thanks', name='thanks'),

    url(r'^user/purchases/new$', login_required(PurchaseOrderCreate.as_view()), name='new_purchase'),
    url(r'^user/purchases$', login_required(PurchasesView.as_view()), name='user_purchases'),
    url(r'^user/purchase/(?P<pk>[\w-]+)/edit$', login_required(PurchaseOrderUpdate.as_view()), name='edit_purchase'),
    url(r'^user/purchase/(?P<pk>[\w-]+)$', login_required(PurchaseOrderDelete.as_view()), name='purchase'),

    url(r'^$', auth_views.login, {'template_name': 'home.html', 'authentication_form': LoginForm }, name = 'home'),
    url(r'^reset/$', 'users.views.reset_psw',name='reset_psw'),

    url(r'^reset/confirm/(?P<uid>\w+)/(?P<token>[-\w]+)/$', 'users.views.reset_psw_confirm', name = 'reset_psw_confirm'),

    url(r'^logout/$', auth_views.logout, {'template_name': 'user.html','next_page':'/'}, name='logout'),


    # url(r'^payroll/', include('payroll.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

)