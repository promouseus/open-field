from django.forms import ModelForm
from .models import Logbook


class LogbookForm(ModelForm):
    class Meta:
        model = Logbook
        fields = '__all__'
        #fields = ['employee', 'customer', 'task', 'date', 'minutes', 'description', 'billable']
