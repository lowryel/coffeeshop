from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from coffee.models import *
from user_accounts.views import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OrderReservationForm, TestimonialForm
from django.utils.translation import pgettext
from django.core.paginator import Paginator
from django.db.models import Sum
from django.views.generic import CreateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin


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

#Display for About page



def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']

        contact_us=ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
        contact_us.save()
        messages.success(request, "Customer message received successfully")
        return redirect('contact')
    else:   
        return render(request, 'coffee/contact.html')


def index(request):

    return render(request, 'coffee/index.html')

def service(request):

    return render(request, 'coffee/service.html')

def about(request):

    return render(request, 'coffee/about.html')



def reservation(request):
    form=OrderReservationForm(request.POST or None)
    if form.is_valid():

        if request.user.is_authenticated:
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            messages.success(request, "Order booking is successful")
            return redirect('menu')
        else:
            return redirect("menu")
    
    return render(request, 'coffee/reservation.html', {"form":form})




class TestimonialCreateView(LoginRequiredMixin, CreateView):
    queryset=Testimonial.objects.all()
    login_url="/login/"
    form=TestimonialForm
    template_name='coffee/testimonial.html'
    # success_url= 'menu'
    fields=['client', 'profession', 'comment']

    def form_valid(self, form):
        instance=form.save(commit=False)
        instance.user=self.request.user
        return super(TestimonialCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['queryset']=self.queryset
        return context


# Display for the menu page
def menu(request):

    return render(request, 'coffee/menu.html')

# def delete_order(request, id):
#     OrderBooking.objects.filter(id=id).delete()
#     orders=OrderBooking.objects.in_bulk()

#     context={'orders':orders}
#     return render(request, 'delete.html', context)

    

