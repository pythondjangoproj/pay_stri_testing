from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = "sk_test_51KwAMcLxyVxYiPi7gkU8ulNBJztSiGgLl5rBGhVlstPFdottXXL3bwNW6mJtGy05xf16QnitTtgxWx0OoFjCtLQN00BBCJOa4e"


# Create your views here.

def index(request):
    return render(request, 'stripe_app/index.html')


def charge(request):
    if request.method == 'POST':
        print('Data:', request.POST)

        amount = int(request.POST['amount'])

        customer = stripe.Customer.create(
            email=request.POST['email'],
            name=request.POST['nickname'],
            source=request.POST['stripeToken']
        )

        charge = stripe.Charge.create(
            customer=customer,
            amount=amount * 100,
            currency='usd',
            description="Donation"
        )

    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
    amount = args
    return render(request, 'stripe_app/success.html', {'amount': amount})
