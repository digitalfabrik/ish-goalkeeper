"""
Privacy information for users
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def privacy_statement(request):
    """
    Show privacy statement
    """
    return render(request, 'privacy.html')
