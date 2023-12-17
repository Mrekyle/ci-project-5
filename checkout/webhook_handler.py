from django.http import HttpResponse


class StripeWH_Handler:
    """
        Stripe webhook handler
    """

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

    def handle_payment_intent_succeeded(self, event):
        """
            Handle the payment intent succeeded. After the
            payment was successful 
        """

        intent = event.data.object
        print(intent)

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
