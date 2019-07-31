"""
User profile editing in the front end.
"""
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


@csrf_protect
@login_required
def edit_profile(request):
    """
    Profile editing form
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if 'old_password' in request.POST:
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Passwort geändert!')
                return redirect('edit_profile')
            else:
                messages.error(request, 'Fehlerhafte Passwort-Eingabe.')
        elif 'email' in request.POST:
            try:
                validate_email(request.POST['email'])
                valid_email = True
            except ValidationError:
                valid_email = False
            if valid_email:
                print("valid e-mail")
                request.user.email = request.POST['email']
                request.user.save()
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile.html', {
        'pw_form': form
    })
