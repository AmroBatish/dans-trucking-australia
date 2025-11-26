from django.contrib import admin
from .models import Client, Service, Equipment,  NewsletterSubscription, QuoteRequest

# admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Equipment)

admin.site.register(NewsletterSubscription)

class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('location', 'person', 'destination', 'contact', 'status', 'created_at')  # عرض الحقول التي تهمك
    search_fields = ['location', 'person', 'destination', 'contact']
admin.site.register(QuoteRequest, QuoteRequestAdmin)

class ClientAdmin(admin.ModelAdmin):
    # تأكد من أن الإعدادات في الـ Admin تعمل بشكل صحيح
    list_display = ('full_name', 'email', 'phone', 'address', 'message')

admin.site.register(Client, ClientAdmin)