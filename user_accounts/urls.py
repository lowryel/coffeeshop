from django import template
from django.urls import path
from user_accounts.views import *


urlpatterns = [
    path('register', upload_file, name='register'),
    path('list_order/<int:pk>', ListOrderView.as_view(), name='list_order'),
    path('signup', UserRegister.as_view(template_name='accounts/signup.html'), name='signup'),
    path('accounts/profile/', profile, name='profile'),
]


