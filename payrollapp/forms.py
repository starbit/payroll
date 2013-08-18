# coding: utf-8

from django import forms
from payrollapp.models import PurchaseOrder

class PurchaseOrderForm(forms.ModelForm):
    amount = forms.DecimalField(label=u"金额")
    description = forms.CharField(label=u"描述")
    time = forms.DateTimeField(label=u"时间")

    class Meta:
        model = PurchaseOrder
        exclude = ['user']