# coding: utf-8
from django.views.generic.edit import FormView, UpdateView, DeleteView
from payrollapp.models import PurchaseOrder
from payrollapp.forms import PurchaseOrderForm
from django.views.generic import ListView

class ReqListView(ListView):
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        c = super(ReqListView, self).get_context_data(**kwargs)
        # add the request to the context
        c.update({ 'request': self.request })
        return c

class PurchasesView(ReqListView):
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return user.purchaseorder_set.all()

    def get_template_names(self):
        return "payrollapp/purchases.html"

class PurchaseOrderCreate(FormView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    success_url = '/user/purchases'
    template_name = "payrollapp/purchaseorder_form.html"

    def form_valid(self, form):
        purchase = form.save(commit=False)
        purchase.user_id = self.request.user.id
        purchase.save()
        return super(PurchaseOrderCreate, self).form_valid(form)

class PurchaseOrderUpdate(UpdateView):
    form_class = PurchaseOrderForm
    template_name = "payrollapp/purchaseorder_form.html"
    success_url = '/user/purchases'

    def get_object(self):
        return self.request.user.purchaseorder_set.get(pk=self.kwargs['pk'])

class PurchaseOrderDelete(DeleteView):
    success_url = '/user/purchases'

    def get_object(self):
        return self.request.user.purchaseorder_set.get(pk=self.kwargs['pk'])