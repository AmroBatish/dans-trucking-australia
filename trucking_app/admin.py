from django.contrib import admin
from .models import Client, Service, Equipment,  NewsletterSubscription

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Equipment)

admin.site.register(NewsletterSubscription)

