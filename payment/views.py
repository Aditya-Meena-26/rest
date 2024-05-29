# views.py

import stripe
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseBadRequest

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request, product_price):
    # Convert USD to INR (Indian Rupees) using the current exchange rate
    # Example conversion rate: 1 USD = 75 INR
    INR_conversion_rate = 75

    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        if not token:
            return HttpResponseBadRequest("Stripe token not provided")
        
        try:
            # Convert product price to INR
            product_price_INR = product_price * INR_conversion_rate
            
            charge = stripe.Charge.create(
                amount=int(product_price_INR * 100),  # Convert price to cents
                currency='inr',  # Use INR as the currency
                description='Product purchase',
                source=token,
            )
        except stripe.error.CardError as e:
            # Display error to user
            return render(request, 'payment_error.html', {'error': e})
        return render(request, 'payment_success.html')
    
    # Pass product price and currency to the template
    return render(request, 'checkout.html', {'product_price': product_price, 'currency': 'INR'})
