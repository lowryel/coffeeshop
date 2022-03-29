from pyexpat import model
from coffee.models import Testimonial
# from django.forms import ModelForm
from django import forms
from coffee.models import OrderBooking


class TestimonialForm(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields=['client', 'profession', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        }


class OrderReservationForm(forms.ModelForm):
    class Meta:
        model=OrderBooking
        fields=['menu_name', 'email', 'persons']




# menu_name=
# email=model
# date=model
# time=model
# persons=mo