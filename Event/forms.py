from django.forms import ModelForm
from .models import Event

from django import forms


class DateInput(forms.DateInput):
    
    input_type ='date'


class EventForm(ModelForm):
    class Meta:
        model=Event
        fields = '__all__'
         
        
        widgets={'evt_date':DateInput()}
        
        exclude=('nbr_participants','state','participant',)
        
    