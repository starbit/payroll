# -*- coding: utf-8 -*-

def home(request):
    if request.method == 'POST':
        form = Login
    return TemplateResponse(request, '')