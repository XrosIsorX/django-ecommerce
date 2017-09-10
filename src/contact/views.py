# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm

def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        print(form.cleaned_data['name'])
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from MYSITE.com'
        emailForm = form.cleaned_data['email']
        message = '%s %s %s' %(emailForm, comment, name)
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailForm, emailTo, fail_silently=True)
        title = 'Thanks!'
        confirm_message = 'Thank for the message. We will get right back to you.'
        form = None

    context = {'title': title, 'form': form, 'confirm_message': confirm_message, }
    template = 'contact.html'
    return render(request,template,context)
