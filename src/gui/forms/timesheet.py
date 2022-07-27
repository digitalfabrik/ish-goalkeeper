"""
Form for entering time
"""
from django.forms import ModelForm, SelectDateWidget
from django.forms import BaseFormSet
from ..models import TimeSheet


class TimeSheetForm(ModelForm):
    """
    Form class
    """
    class Meta:
        """
        meta information
        """
        model = TimeSheet
        fields = ['course', 'hours', 'rate', 'date']
        widgets = {
            'date': SelectDateWidget(),
        }

class BaseTimeSheetFormSet(BaseFormSet):
    """
    Formset to pass request arg
    """
