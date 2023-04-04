from django.contrib import admin

from shop.models import Subcategories, Categories, Product

# Register your models here.

admin.site.register(Subcategories)
admin.site.register(Categories)
admin.site.register(Product)