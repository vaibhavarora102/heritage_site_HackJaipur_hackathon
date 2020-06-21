from django.contrib import admin
from .models import Profile, OrderItem, Order, Transaction

admin.site.register(Profile)
# for shoping cart------------------------------------------------------------------------------------------------------------
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Transaction)
#end==========================================================================================================================