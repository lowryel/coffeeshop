from django import template
from django.urls import path
from user_accounts.views import *


urlpatterns = [
    path('register', upload_file, name='accounts/register'),
    path('list_order', ListOrderView.as_view(), name='accounts/list_order'),
    path('accounts/profile/', profile, name='accounts/profile'),
]


