from django import template

register = template.Library ()


@register.filter (name='is_in_cart')
def is_in_cart(service, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == service.id:
            return True
    return False;


@register.filter (name='cart_quantity')
def cart_quantity(service, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == service.id:
            return cart.get (id)
    return 0;


@register.filter (name='price_total')
def price_total(service, cart):
    return service.price * cart_quantity (service, cart)


@register.filter (name='total_cart_price')
def total_cart_price(services, cart):
    sum = 0;
    for p in services:
        sum += price_total (p, cart)

    return sum
