from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path("", views.home, name="home"),              # index.html
    path("about/", views.about, name="about"),      # about.html
    path("services/", views.services, name="services"),  # services.html
    path("equipments/", views.equipments, name="equipments"),  # equipments.html
    path('equipment/<int:id>/', views.equipment_detail, name='equipment_detail'),
    path("contacts/", views.contacts, name="contact"),  # contacts.html
    path('tractors/', views.tractors, name='tractors'),
    # صفحة تفاصيل خدمة
    path("services/<int:id>/", views.service_detail, name="service_detail"),
    path('get-quote/', views.get_quote, name='get_quote'),
    path("subscribe/", views.subscribe, name="subscribe"),
    path('request-quote/', views.request_quote_view, name='request_quote'),
    path('contact/', views.contact_view, name='contact_view'),  # إضافة URL للـ contact view
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    