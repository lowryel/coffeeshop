import email
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

from coffee.models import OrderBooking
from .forms import UserRegisterForm
from django.urls import reverse_lazy
from django.views import View
from django.views. generic import ListView

# Create your views here.

class RegisterView(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'accounts/register.html')

class ListOrderView(View):

    def get(self, request, *args, **kwargs):
        order_listing=OrderBooking.objects.all().order_by('date', 'time')
        context={"order_listing":order_listing}
        return render(request, 'accounts/list_order.html', context)


class UserRegister(SuccessMessageMixin, CreateView):
    model=User
    form_class=UserRegisterForm
    success_url=reverse_lazy('coffee/menu')
    template="accounts/register.html"
    def form_valid(self, form):
        super(UserRegister, self).form_valid(form)
        user=authenticate(self.request, username=form.cleaned_data['username'], 
        password=form.cleaned_data['password1'])
        if user==None:
            return self.render_to_response(self.get_context_data(form=form))
        login(self.request, user)
        return redirect(self.get_success_url())



