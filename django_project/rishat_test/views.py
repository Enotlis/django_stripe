from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import stripe
from .models import Item

def get_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    publish_key = settings.PUBLISH_STRIP_KEY
    context = {'item': item, 'item_id': item_id, 'pb_key': publish_key}
    return render(request, 'item.html', context)

def buy_item(request, item_id):
    stripe.api_key = settings.SECRET_STRIP_KEY
    item = Item.objects.get(pk=item_id)
    session = stripe.checkout.Session.create(
    line_items=[{
        'price_data': {
            'currency': item.get_currency_display(),
            'product_data': {
                'name': item.name,
            },
            'unit_amount': int(item.price * 100),
        },
        'quantity': 1,
    }],
    mode='payment',
    success_url=f'http://{settings.URL}{reverse("success")}',
    cancel_url=f'http://{settings.URL}{reverse("get_item", kwargs={"item_id": item_id})}',
    )

    return JsonResponse({'session': session})

def success(request):
    return render(request, 'success.html')