from django import template
from store.models.order import Order

register = template.Library()

@register.simple_tag
def count_pending_orders():
    pending_orders = Order.objects.filter(status=False).count()  # Replace 'status' with your order status field
    return pending_orders