from django.urls import reverse
from django.conf import settings
from django.db import models
User=settings.AUTH_USER_MODEL

from django.db.models.signals import post_save
from django.dispatch import receiver

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

def email_validator(email):
        if 'com' in email.split('.'):
            return 'Valid email'
        else:
            return 'Invalid email. Make sure your email is a .com'

class ContactUs(models.Model):
    name=models.CharField(max_length=150, blank=False)
    email=models.EmailField(validators=[email_validator])
    subject=models.CharField(max_length=120, blank=False)
    message=models.TextField(blank=True, editable=True)

    
    def __str__(self):
        return self.name

@receiver(post_save, sender=OrderBooking)
def testimonial_post_save(sender, created, **kwargs):
    print(sender, created)


class Testimonial(models.Model):
    client=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    profession=models.CharField(max_length=150, blank=True)
    comment=models.TextField(blank=False)
    
    def get_absolute_url(self):
        # return "menu"
        return reverse('coffee/menu')

@receiver(post_save, sender=Testimonial)
def testimonial_post_save(sender, created, **kwargs):
    print(sender, created)
