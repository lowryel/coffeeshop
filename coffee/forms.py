from coffee.models import Testimonial
from django import forms
from .models import OrderBooking


class TestimonialForm(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields=['client', 'profession', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        }
# @receiver(post_save, sender=TestimonialForm)
# def testimonial_post_save(sender, created, **kwargs):
#     print(sender, created, **kwargs)

class OrderReservationForm(forms.ModelForm):
    class Meta:
        model=OrderBooking
        fields=['menu_name', 'email', 'persons']



# menu_name=
# email=model
# date=model
# time=model
# persons=mo