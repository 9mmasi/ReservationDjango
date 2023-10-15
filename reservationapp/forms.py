from .models import Reservation
from django.forms import ModelForm, widgets

from django import forms

class AMPMTimeInput(forms.TimeInput):
    input_type = 'time'  # Set the input type to 'time'

    def format_value(self, value):
        if value:
            return value.strftime('%I:%M %p')  # Format time with AM/PM
        return super().format_value(value)


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'Date_checkIn': widgets.DateInput(attrs={'placeholder': 'Check-in date: YYYY-MM-DD',"type":"date"}),
            'Date_checkOut': widgets.DateInput(attrs={'placeholder': 'Check-out date: YYYY-MM-DD',"type":"date"}),
            'Time_checkIn': AMPMTimeInput(attrs={'placeholder': 'Check-in Time',"type":"time"}),
            'Time_checkOut': AMPMTimeInput(attrs={'placeholder': 'Check-out Time',"type":"time"})
        }


class ReservationUpdateForm(ModelForm):
    class Meta:
        model = Reservation
        exclude=['Date_checkIn','Date_checkOut','Time_checkIn','Time_checkOut']