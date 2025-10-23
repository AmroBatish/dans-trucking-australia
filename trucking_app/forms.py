
from django import forms
from .models import QuoteRequest
from .models import  NewsletterSubscription

class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['location', 'person', 'destination', 'contact', 'message']

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={
                "placeholder": "Enter your email...",
                "class": "form-control newsletter-input"
            })
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if NewsletterSubscription.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already subscribed!")
        return email
