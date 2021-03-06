"""
Contact form for users
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect
from django.conf import settings

@login_required
def contact_form(request):
    """
    Contact form for users to contact the admin
    team.
    """
    return render(request, 'contact.html')


@login_required
def send_contact_form(request):
    """
    Send contact form via e-mail to admin team.
    """
    if 'message' not in request.POST:
        return HttpResponseRedirect("/gui/contact/")
    email = EmailMessage('ISH Goalkeeper - Benachrichtigung',
                         request.POST['message'],
                         reply_to=[request.user.email],
                         from_email=settings.EMAIL_HOST_USER,
                         to=[settings.EMAIL_CONTACT])
    email.send()
    return render(request, 'contact.html', context={"sent": True})
