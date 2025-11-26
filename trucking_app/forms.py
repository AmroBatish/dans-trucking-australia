
from django import forms
from .models import QuoteRequest
from .models import  NewsletterSubscription
from .models import Client

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
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'phone', 'address', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Phone',
                'class': 'form-control',
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Address',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'How can we help?',
                'class': 'form-control',
                'rows': 4,
            }),
        }
