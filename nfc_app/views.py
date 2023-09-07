from django.shortcuts import render
from django.http import JsonResponse

from .models import NFCData

def nfc_data(request):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        content = request.POST.get('content')

        nfc_data = NFCData(card_id=card_id, content=content)
        nfc_data.save()

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})