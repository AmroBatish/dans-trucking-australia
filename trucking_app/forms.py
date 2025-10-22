
from django import forms
from .models import QuoteRequest
from .models import  NewsletterSubscription

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['location', 'person', 'destination', 'contact', 'message']

class NewsletterSubscription(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={
                "placeholder": "YOUR E-MAIL",
                "class": "form-control"
            })
        }
