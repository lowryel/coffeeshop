from django.urls import reverse
from django.conf import settings
from django.db import models
User=settings.AUTH_USER_MODEL

# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OrderBooking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    menu_name=models.ForeignKey(Menu, on_delete=models.PROTECT)
    email=models.EmailField()
    date=models.DateField(auto_now_add=True, blank=False)
    time=models.TimeField(auto_now_add=True)
    persons=models.CharField(max_length=120, blank=False)

    def __str__(self):
        return self.menu_name.name


class ContactUs(models.Model):
    name=models.CharField(max_length=150, blank=False)
    email=models.EmailField()
    subject=models.CharField(max_length=120, blank=False)
    message=models.TextField(blank=True, editable=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    profession=models.CharField(max_length=150, blank=True)
    comment=models.TextField(blank=False)
    
    def get_absolute_url(self):
        # return "menu"
        return reverse('coffee/menu')

