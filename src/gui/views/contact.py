"""
Contact form for users
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User  # pylint: disable=E5142

@login_required
def contact_form(request):
    """
    Contact form for users to contact the admin
    team.
    """
    if request.user.groups.filter(name="Lehrkräfte").exists():
        mail_to = settings.EMAIL_CONTACT_TEACHERS
    else:
        mail_to = settings.EMAIL_CONTACT
    context = {
        'pms' : User.objects.filter(groups__name="Projektleitung"),
        'team' : User.objects.filter(groups__name="Team"),
        'mail_to': mail_to,
    }
    if 'message' in request.POST:

        email = EmailMessage('ISH Goalkeeper - Benachrichtigung',
                             request.POST['message'],
                             reply_to=[request.user.email],
                             from_email=settings.EMAIL_HOST_USER,
                             to=[mail_to])
        email.send()
        context["sent"] = True
    return render(request, 'contact.html', context)
