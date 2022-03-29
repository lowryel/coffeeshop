from django.shortcuts import render, redirect
from coffee.models import *
from user_accounts.views import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderReservationForm, TestimonialForm
from django.utils.translation import pgettext
from django.core.paginator import Paginator
from django.db.models import Sum

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
    form=OrderReservationForm(request.POST or None)
    if form.is_valid():

        if request.user.is_authenticated:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            messages.success(request, "Order booking is successful")
            return redirect('coffee/menu')
        else:
            return redirect("coffee/menu")
    
    return render(request, 'coffee/reservation.html', {"form":form})


def service(request):

    return render(request, 'coffee/service.html')

class TestimonialListView(ListView):
    form=TestimonialForm
    template_name='coffee/testimonial.html'
    success_url= 'coffee/menu'
    def testimonial(self, request, form):
        testimony=Testimonial.objects.all()
        order_total=OrderBooking.objects.filter(user=request.user).aggregate(orderbooking_persons=Sum('persons'))
        total_order=order_total['orderbooking_persons']
        if form.is_valid():

            if request.user.authenticated:
                instance=form.save(commit=False)
                instance.user=self.request.user
                instance.save()
                messages.success(request, "Comment submitted")
                return redirect('coffee/menu')
            else:
                return redirect("accounts/register")
        context={
            'testimony': testimony,
            'form':form,
            "total_order":total_order
        }
        return render(request, , context)

# Display for the menu page
def menu(request):

    return render(request, 'coffee/menu.html')
