
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Contact
import json


def contact_view(request):
    if request.method == 'GET':
        return render(request, 'contact.html')

    elif request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        if not all([name, email, phone, subject, message]):
            messages.error(request, 'Zəhmət olmasa bütün sahələri doldurun.')
            return render(request, 'contact.html')

        try:
            contact = Contact.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )

            messages.success(request, 'Mesajınız uğurla göndərildi!')
            return redirect('contact')

        except Exception as e:
            messages.error(
                request, 'Xəta baş verdi. Yenidən cəhd edin.')
            return render(request, 'contact.html')


@csrf_exempt
@require_http_methods(["POST"])
def contact_ajax_view(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        if not all([name, email, phone, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'Zəhmət olmasa bütün sahələri doldurun.'
            }, status=400)

        contact = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return JsonResponse({
            'success': True,
            'message': 'Mesajınız uğurla göndərildi!'
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'Xəta baş verdi. Yenidən cəhd edin.'
        }, status=500)
