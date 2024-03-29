from django import template
from django.urls import path
from user_accounts.views import *


urlpatterns = [
    path('register', upload_file, name='register'),
    path('list_order/', ListOrderView.as_view(), name='list_order'),
    path('signup', UserRegister.as_view(template_name='accounts/signup.html'), name='signup'),
    path('update/<int:pk>', FileUpdateView.as_view(template_name='accounts/profile.html'), name='update'),
    path('accounts/profile/', profile, name='profile'),
    path('delete/<int:pk>', delete, name='delete'),
<<<<<<< Updated upstream
=======
    path('comment/<int:comment_id>', comment, name='comment'),
>>>>>>> Stashed changes
]


