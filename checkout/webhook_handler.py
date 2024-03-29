from django.http import HttpResponse


# The following code was written based on the Code Institute Boutique Ado
# walkthrough and customised to fit this application
class StripeWH_Handler:
    """ Handle Stripe webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle generic/unknown/unexpected webhook events """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """ Handle the payment_intent.succeeded webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """ Handle the payment_intent.payment_failed webhook """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
