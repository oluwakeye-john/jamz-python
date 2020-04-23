from django import forms
from .models import Contact

class NewContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]