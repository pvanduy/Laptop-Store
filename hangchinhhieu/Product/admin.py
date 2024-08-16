from django.contrib import admin

from Product.models import Banner, Brand, Category, Product, BackGroundSale

# Register your models here.
admin.site.register(Banner)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(BackGroundSale)
