# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    secretKey = settings.STRIPE_SECRET_KEY
    print(secretKey)
    print(publishKey)
    print(request.user.userstripe.stripe_id)
    customer_id = request.user.userstripe.stripe_id
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            charge = stripe.Charge.create(
                amount=100000,
                currency="usd",
                customer = customer,
                description="Example charge"
            )
        except stripe.error.CardError as e:
            pass
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request,template,context)
    # user = request.user
    # context = {}
    # template = 'checkout.html'
    # return render(request,template,context)
