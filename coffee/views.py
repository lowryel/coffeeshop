from django.shortcuts import render, redirect
from coffee.models import *
from user_accounts.views import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm
from django.utils.translation import pgettext
from django.core.paginator import Paginator

user=settings.AUTH_USER_MODEL

# Create your views here.
@login_required
def home(request):
    object=['Man', 'Woman', 'She', 'He']
    page= Paginator(object, 2)
    page1=page.page(2)
    print(page1)
    output=pgettext("welcome to my site", "welcome")
    word="Wordle Game"
    context={
        'word':word,
        'output':output,
    }
    return render(request, 'home.html', context)

def about(request):

    return render(request, 'coffee/about.html')


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        contact_us=ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
        contact_us.save()
        messages.success(request, "Customer message received successfully")
        return redirect('coffee/contact')
    else:   
        return render(request, 'coffee/contact.html')


def index(request):

    return render(request, 'coffee/index.html')


def reservation(request):
    if request.user.is_authenticated:

        if request.method=="POST":
            menu_name=request.POST['menu_name']
            email=request.POST['email']
            date=request.POST['date']
            time=request.POST['time']
            persons=request.POST['persons']

            order_booking=OrderBooking.objects.create(menu_name=menu_name, email=email, date=date, time=time, persons=persons)
            order_booking.save()
            messages.success(request, "Order booking is successful")
            return redirect('coffee/contact')
        else:
            return render(request, 'coffee/reservation.html')
    messages.info(request, "You need to login")
    return redirect("coffee/menu")


def service(request):

    return render(request, 'coffee/service.html')

    
@login_required
def testimonial(request):
    testimony=Testimonial.objects.all()
    if request.method=="POST":
        client=request.POST['client']
        profession=request.POST['profession']
        comment=request.POST['comment']
        image=request.POST['image']
        testament=Testimonial.objects.create(client=client, profession=profession,
        comment=comment, image=image)
        testament.save()
        return redirect('coffee/testimonial')

    context={
        'testimony': testimony,
    }
    return render(request, 'coffee/testimonial.html', context)


def menu(request):

    return render(request, 'coffee/menu.html')
