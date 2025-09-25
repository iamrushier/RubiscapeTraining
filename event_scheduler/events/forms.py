from django import forms
from .models import Event
import datetime

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields=['name','date','time','description']
        widgets = {
            'date': forms.DateInput(attrs={
                'type':'date',
                'min':datetime.date.today().strftime('%Y-%m-%d')
            }),
            'time':forms.TimeInput(attrs={
                'type':'time'
            }),
        }