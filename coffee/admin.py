from re import search
from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(OrderBooking)
admin.site.register(ContactUs)
admin.site.register(Testimonial)
# admin.site.register(Menu)

class MenuAdmin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Menu, MenuAdmin)

class OrderBookingAdmin(admin.ModelAdmin):
    list_display=['user', 'menu_name', 'email', 'date', 'time', 'persons']
    list_editable=['menu_name', 'email', 'persons']
    list_per_page=2
    # search_fields=['menu_name']
    

admin.site.register(OrderBooking, OrderBookingAdmin)

