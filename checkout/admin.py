from django.contrib import admin
from .models import Order, OrderLineItem


# The following code was written based on the Code Institute Boutique Ado
# walkthrough and customised to fit this application
class OrderLineItemAdminInLine(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInLine,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total')

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email', 'postcode', 'town_or_city',
              'street_address_1', 'street_address_2',
              'delivery_cost', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
