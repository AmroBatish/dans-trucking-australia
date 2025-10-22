from django.shortcuts import render , get_object_or_404
from django.http import JsonResponse
from .models import Service , Equipment
from .forms import QuoteRequestForm , NewsletterSubscription


def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    # جلب جميع الخدمات من قاعدة البيانات
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


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterSubscription(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'You have successfully subscribed to the newsletter!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request.'})

