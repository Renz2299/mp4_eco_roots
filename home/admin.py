from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'contact_content',
        'sent_on',
    )


admin.site.register(Contact, ContactAdmin)
