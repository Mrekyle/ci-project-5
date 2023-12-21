from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from .models import Order, NewItem
from products.models import Product
from profiles.models import UserProfile

import stripe
import json
import time


class StripeWH_Handler:
    """
        Stripe webhook handler
    """

    def _send_email_confirm(self, order):
        """
            Handles the sending of a confirmation email to the user
        """

        custom_email = order.email
        subject = render_to_string(
            'checkout/confirmation-emails/confirmation_email_subject.txt',
            {'order': order},
        )
        body = render_to_string(
            'checkout/confirmation-emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_CONFIRMATION_EMAIL}
        )
        send_mail(
            subject,
            body,
            settings.DEFAULT_CONFIRMATION_EMAIL,
            [custom_email]
        )

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
            Handle the generic, unknown and unexpected
            webhook events
        """

        return HttpResponse(
            content=f'Unhandled Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event, order):
        """
            Handle the payment intent succeeded. After the
            payment was successful 
        """

        intent = event.data.object
        pid = intent.pid
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe.charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        for field, value in shipping_details.address_items():
            if value == '':
                shipping_details.address[field] = None

        profile = None
        username = intent.metadata.username

        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.def_phone_number = shipping_details.phone
                profile.def_street_address1 = shipping_details.street_address1
                profile.def_street_address2 = shipping_details.street_address2
                profile.def_town_or_city = shipping_details.town_or_city
                profile.def_county = shipping_details.country
                profile.def_country = shipping_details.country
                profile.def_postcode = shipping_details.postcode
                profile.save()

        order_exists = False
        attempt = 1

        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.name,
                    phone_number__iexact=shipping_details.phone,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.staticmethod,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    grand_total=grand_total,
                    stripe_pid=pid,
                    original_bag=bag,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

            if order_exists:
                self._send_email_confirm(order)
                return HttpResponse(
                    content=f'Webhook {event["type"]} | SUCCESS: New order created in database', status=200
                )
            else:
                order = None
                try:
                    order = Order.objects.create(
                        full_name=shipping_details.name,
                        user_profile=profile,
                        email=billing_details.name,
                        phone_number=shipping_details.phone,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.staticmethod,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        grand_total=grand_total,
                        stripe_pid=pid,
                        original_bag=bag,
                    )
                    for item_id, item_data in json.loads(bag).items():
                        product = Product.objects.get(id=item_id)
                        if isinstance(item_data, int):
                            new_line_item = NewItem(
                                order=order,
                                product=product,
                                quantity=item_data,
                            )
                            new_line_item.save()
                except Exception as e:
                    if order:
                        Order.delete()
                    return HttpResponse(
                        content=f'Webhook: {event["type"]} | ERROR: {e}', status=500
                    )

        self._send_email_confirm(order)
        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
            Handle the payment intent fail webhook from stripe.
            If the payment has failed
        """

        return HttpResponse(
            content=f'Webhook Received: {event["type"]}',
            status=200)
