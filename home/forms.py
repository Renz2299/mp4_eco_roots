from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'contact_content')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
