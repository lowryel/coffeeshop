from coffee.models import Testimonial
from django.forms import ModelForm
from django import forms

class TestimonialForm(ModelForm):
    class Meta:
        model=Testimonial
        fields="__all__"
        widgets = {
            'comment': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        }



