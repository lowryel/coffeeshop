from django import template
from django.urls import path
from user_accounts.views import *


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('list_order', ListOrderView.as_view()),
]


