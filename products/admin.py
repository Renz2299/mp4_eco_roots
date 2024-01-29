from django.contrib import admin
from .models import Product, Category, Review


# The following code was written based on the Code Institute Boutique Ado
# walkthrough and customised to fit this application
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )
# End of customised code from Boutique Ado walkthrough


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'title',
        'rating',
        'date',
    )

    ordering = ('date',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
