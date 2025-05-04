from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import *
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Productdark)
admin.site.register(Producttan)
admin.site.register(Productage)
admin.site.register(Productagehair)
admin.site.register(Productdan)
admin.site.register(Productfri)
admin.site.register(Productperfumes)
admin.site.register(Productbath)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


