from django.conf.urls import patterns, include, url
from users.forms import LoginForm
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

class ReqListView(ListView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        c = super(ReqListView, self).get_context_data(**kwargs)
        # add the request to the context
        c.update({ 'request': self.request })
        return c

class UserPurchaseView(ReqListView):
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return user.purchaseorder_set.all()

    def get_template_names(self):
        return "users/purchases.html"


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^user/$', 'users.views.user', name='user'),
    url(r'^user/arrive$', 'users.views.arrive', name='user_arrive'),
    url(r'^user/leave$', 'users.views.leave', name='user_leave'),
    url(r'^user/add_purchase$', 'users.views.add_purchase', name='user_add_purchase'),
    url(r'^user/purchases$', login_required(UserPurchaseView.as_view()), name='user_purchases'),

    url(r'^$', auth_views.login, {'template_name': 'home.html', 'authentication_form': LoginForm }, name = 'home'),
    url(r'^reset/$', 'users.views.reset_psw',name='reset_psw'),

    url(r'^reset/confirm/(?P<uid>\w+)/(?P<token>[-\w]+)/$', 'users.views.reset_psw_confirm', name = 'reset_psw_confirm'),

    url(r'^user/logout/$', auth_views.logout, {'template_name': 'user.html','next_page':'/'}, name='logout'),


    # url(r'^payroll/', include('payroll.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
