from django import forms
from .models import Contact


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['user_name', 'user_email', 'user_phone', 'user_review']
