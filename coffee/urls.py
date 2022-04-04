
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='coffee/about'),
    path('contact', contact, name='coffee/contact'),
    path('index', index, name='coffee/index'),
    path('reservation', reservation, name='coffee/reservation'),
    path('service', service, name='coffee/service'),
    path('menu', menu, name='coffee/menu'),
    # path('testimonial', testimonial, name='coffee/testimonial'),
    path('testimonial', TestimonialCreateView.as_view(), name='coffee/testimonial'),
    path('login/', LoginView.as_view(), name="coffee/login")
]



 


