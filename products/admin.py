from django.contrib import admin

from products.models import Category, Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name', 'price')
    list_filter = ('category',)
    list_display = ('name', 'price', 'category')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
