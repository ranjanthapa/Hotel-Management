import stripe
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
from room.models import RoomDetail

stripe.api_key = STRIPE_SECRET_KEY


class PaymentView(TemplateView):
    template_name = 'payment/payment_home.html'


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_configue = {'publiceKey': STRIPE_PUBLISHABLE_KEY}

        return JsonResponse(stripe_configue, safe=False)


class CreateSessionCheckOutView(View):
    def post(self, request, *args, **kwargs):
        room_detail = RoomDetail.objects.get(room=self.kwargs['pk'])
        domain = get_current_site(request)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 20000,
                        'product_data': {
                            'name': room_detail.room_type,
                        }
                    }
                }
            ],
            mode='payment',
            success_url=f"http://{domain}/success",
            cancel_url=f"http://{domain}/cancel",
        )
        return redirect(checkout_session.url)
