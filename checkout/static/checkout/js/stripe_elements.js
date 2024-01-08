var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: '#778c68',
        fontFamily: '"Duru Sans", sans-serif',
        fontSize: '16px',
        '::placeholder': {
            color: '#2e4013',
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545',
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');