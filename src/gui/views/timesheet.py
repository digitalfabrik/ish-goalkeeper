"""
Contact form for users
"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.contrib import messages
from ..forms import TimeSheetForm, BaseTimeSheetFormSet
from ..models import Course

@login_required
def timesheet(request):
    """
    Contact form for users to contact the admin
    team.
    """
    TimeSheetFormSet = formset_factory(TimeSheetForm, formset=BaseTimeSheetFormSet, extra=5)
    if request.method == 'POST':
        formset = TimeSheetFormSet(request.POST)
        for form in formset:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.instructor = request.user
                instance.save()
                messages.add_message(
                    request,
                    messages.INFO,
                    f"{instance.hours} Stunden für {instance.course} "
                    f"am {instance.date} gespeichert.")
    formset = TimeSheetFormSet()
    return render(request, 'timesheet.html', context={'formset': formset})
