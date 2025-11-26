from django.shortcuts import render , get_object_or_404, redirect
from django.http import JsonResponse
from .models import Service , Equipment 
from .forms import QuoteRequestForm, NewsletterSubscriptionForm, ClientForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Equipment, NewsletterSubscription


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    services = Service.objects.all()  
    return render(request, 'services.html', {'services': services})

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    services = Service.objects.all()  # Get all services for the menu
    
    # Check if request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = {
            'name': service.name,
            'image': service.image.url if service.image else '',
            'description': service.description,
        }
        return JsonResponse(data)
    
    return render(request, 'service_detail.html', {
        'service': service,
        'services': services  # Pass all services for the menu
    })


def equipments(request):
    # جلب جميع المعدات من قاعدة البيانات
    equipments = Equipment.objects.all()  # إحضار كل المعدات
    return render(request, 'equipments.html', {'equipments': equipments})

def equipment_detail(request, id):
    equipment = get_object_or_404(Equipment, id=id)
    equipments = Equipment.objects.all()  # Get all equipments for the menu
    
    # Check if request is AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        data = {
            'name': equipment.name,
            'image': equipment.image.url if equipment.image else '',
            'description': equipment.description,
        }
        return JsonResponse(data)
    
    return render(request, 'equipment_detail.html', {
        'equipment': equipment,
        'equipments': equipments  # Pass all equipments for the menu
    })

def contacts(request):
    return render(request, "contacts.html")

def tractors(request):
    return render(request, 'tractors.html')

def get_quote_ajax(request):
    # منطق الدالة هنا
    return JsonResponse({'quote': 'بعض البيانات الخاصة بالعرض'})


def get_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ الطلب في قاعدة البيانات
            return JsonResponse({'success': True, 'message': 'Your quote request has been submitted successfully.'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    
    return JsonResponse({'success': False, 'message': 'Invalid request.'})


from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from .models import NewsletterSubscription
import logging

logger = logging.getLogger(__name__)


def subscribe(request):
    if request.method == 'POST':
        try:
            logger.info('Subscribe endpoint called', extra={'path': request.path})
            # Log minimal request info for debugging (avoid logging sensitive data)
            logger.debug('Subscribe request POST keys: %s', list(request.POST.keys()))
        except Exception:
            # non-fatal logging error
            pass
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            try:
                send_mail(
                    subject='Newsletter Subscription Confirmation',
                    message='Thank you for subscribing to our newsletter! You will now receive updates and news from us.',
                    from_email=getattr(settings, 'DEFAULT_FROM_EMAIL', None) or getattr(settings, 'EMAIL_HOST_USER', None),
                    recipient_list=[subscription.email],
                    fail_silently=False,
                )
            except Exception as e:
                logger.exception('Failed to send subscription confirmation email')
                # Return a JSON response with the error so the frontend can show it
                return JsonResponse({
                    'success': False,
                    'message': 'Subscription saved but failed to send confirmation email.',
                    'error': str(e),
                }, status=500)

            return JsonResponse({
                'success': True,
                'message': '✅ You have successfully subscribed! A confirmation email has been sent.'
            })
        else:
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request.'}, status=400)


from django.http import JsonResponse
from .forms import QuoteRequestForm


def request_quote_view(request):
    # Accept AJAX posts regardless of header case; jQuery sends 'XMLHttpRequest'
    if request.method == "POST" and request.headers.get('X-Requested-With', '').lower() == 'xmlhttprequest':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Your request has been submitted successfully! Our specialists will contact you shortly.'}, status=200)
        else:
            return JsonResponse({'message': 'There was an error submitting your request. Please try again later.'}, status=400)
    else:
        form = QuoteRequestForm()

    return render(request, 'quote_request_form.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to the database

            # بدل request.is_ajax()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Your message has been sent successfully!'})

            return redirect('contact_success')  # لو مو Ajax

        else:
            # في حال وجود أخطاء بالفورم
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse(
                    {
                        'message': 'There was an error with the data entered. Please check the fields!',
                        'errors': form.errors,   # مهم عشان الأجاكس يستخدمها
                    },
                    status=400
                )

            return render(request, 'contact.html', {'form': form})

    else:
        form = ClientForm()

    return render(request, 'contact.html', {'form': form})