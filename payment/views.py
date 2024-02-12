import json

import stripe
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from core.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
from room.models import RoomDetail, Room, Reservation, BookingConfirmation

stripe.api_key = STRIPE_SECRET_KEY
end_point_secret = "whsec_55420383babc2444875d7a77eddeaf9027477f87b9dab9870f376550ed3ede13"


class PaymentView(TemplateView):
    template_name = 'payment/payment_home.html'


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_configue = {'publiceKey': STRIPE_PUBLISHABLE_KEY}

        return JsonResponse(stripe_configue, safe=False)


class CreateSessionCheckOutView(View):

    def get(self, request, *args, **kwargs):
        try:
            room_uid = urlsafe_base64_decode(self.kwargs['room_uid']).decode()
            print(room_uid)
            reservation_uid = urlsafe_base64_decode(self.kwargs['reservation_uid']).decode()
            print(reservation_uid)
        except Exception as e:
            print(e)
        # room_obj = Room.objects.get(room_no=room_uid)

        reservation_obj = Reservation.objects.get(pk=reservation_uid)
        # print(reservation_obj)
        # if not reservation_obj.exists():
        #     pass

        room_detail = RoomDetail.objects.filter(room__room_no=room_uid).first()

        domain = get_current_site(request)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            phone_number_collection={
                'enabled': True,
            },
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': room_detail.price,
                        'product_data': {
                            'name': room_detail.room_type + "bed",
                        }
                    },
                    'quantity': 1,
                }
            ],
            metadata={
                'room_no': room_uid,
                'reservation_id': reservation_uid
            },

            mode='payment',
            customer_email=reservation_obj.email,
            # customer_number = reservation_obj.phone_number,
            success_url=request.build_absolute_uri(reverse('room:reservation')) + f'?confirm=True',
            cancel_url=f"http://{domain}/cancel",
        )
        return redirect(checkout_session.url)


@method_decorator(csrf_exempt, name='dispatch')
class StripeWebHookerView(View):

    def post(self, request):
        payload = request.body
        print(json.dump(payload, indent=4))
        event = None
        sig_header = request.headers['STRIPE_SIGNATURE']

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, end_point_secret
            )
            print(event)
        except ValueError as e:
            return HttpResponse(status=400)
        except stripe.errors.SignatureVerificationError as e:
            print("Errorr")
        if event['type'] == 'checkout.session.completed':
            room_number = event['metadata']['room_no']
            print(f'inside of webhooook and the number is {room_number}')
            reservation_id = event['metadata']['reservation_id']
            print(f'inside of webhooook and the number is {reservation_id}')
            booking_instance, exists = BookingConfirmation.objects.get_or_create(reservation_id=reservation_id)
            if exists:
                booking_instance.payment = True
            else:
                booking_instance.room.add(room_number)
                booking_instance.payment = True
            return HttpResponse(status=200)

        else:
            print(f"{event.type}")
        return HttpResponse(status=200)
