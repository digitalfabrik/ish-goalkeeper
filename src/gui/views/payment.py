"""
View for payments
"""

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import Payment

@login_required
def payment(request):
    """
    Show payment form
    """
    payment = Payment
    context = {
        'payment' : payment
    }
    return render(request, 'payment.html', context)