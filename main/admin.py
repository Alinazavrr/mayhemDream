from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(ProductType)
admin.site.register(News)
admin.site.register(Purchase)


