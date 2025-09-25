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
    def __init__(self, *args, **kwargs):
        self.user=kwargs.pop("user",None)
        super().__init__(*args,**kwargs)
        
    def clean(self):
        cleaned_data=super().clean()
        date=cleaned_data.get("date")
        time=cleaned_data.get("time")
        if self.user and date and time:
            # query set
            qs=Event.objects.filter(user=self.user, date=date, time=time)
            
            if self.instance.pk: # if pk exists -> means update
                qs=qs.exclude(pk=self.instance.pk)
                
            if qs.exists():
                self.add_error("time","Err: You already have and event at this date and time")
        return cleaned_data