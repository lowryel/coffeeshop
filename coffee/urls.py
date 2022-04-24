
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('index', index, name='index'),
    path('reservation', reservation, name='reservation'),
    path('service', service, name='service'),
    path('menu', menu, name='menu'),
    path('testimonial', TestimonialCreateView.as_view(), name='testimonial'),
    path('login', LoginView.as_view(), name="login")
]



 


