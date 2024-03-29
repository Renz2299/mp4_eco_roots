from django import forms
from .models import Order


# The following code was written based on the Code Institute Boutique Ado
# walkthrough and customised to fit this application
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'street_address_1',
                  'street_address_2', 'town_or_city', 'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'street_address_1': 'Street Address 1',
            'street_address_2': 'Street Address 2',
            'town_or_city': 'Town or City',
            'postcode': 'Postal Code',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
