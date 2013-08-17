from django.conf.urls import patterns, include, url
from users.forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    url(r'^user/$', 'users.views.user', name='user'),
                       
    url(r'^$', auth_views.login, {'template_name': 'home.html', 'authentication_form': LoginForm }, name = 'home'),
                       
                       
    url(r'^reset/$', 'users.views.reset_psw',name='reset_psw'),
                       
    url(r'^reset/confirm/(?P<uid>\w+)/(?P<token>[-\w]+)/$', 'users.views.reset_psw_confirm', name = 'reset_psw_confirm'),
                       
    url(r'^user/logout/$', auth_views.logout, {'template_name': 'user.html','next_page':'/'}, name='logout'),


    # url(r'^payroll/', include('payroll.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
