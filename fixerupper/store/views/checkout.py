from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from store.models.userprofile import UserProfile
from django.views import View
from store.models.provider import Provider
from store.models.service import Services
from store.models.order import Order, Notification

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user_id = request.session.get('user')
        cart = request.session.get('cart')
        services = Services.get_services_by_id(list(cart.keys()))
        print("Address: " +  address)
        print("Phone: "  + phone)
        # print(f'User:{user}')
        print(f'Cart:{cart}')
        print(f'Services: {services}')

        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            return redirect('/login')


        for service in services:
            print(cart.get(str(service.id)))
            order = Order(user=UserProfile.objects.get(user_id=user_id),
                            service=service,
                            price=service.price,
                            phone=phone,
                            address=address,
                            quantity=cart.get(str(service.id)))
          
            order.save()
          
            providers = service.providers.all()
            for provider in providers:
                if service in provider.services_offered.all():
                    notification = Notification(
                        order=order,
                        provider=provider.user_profile,
                        message=f"New order placed for {service.name}. Order ID: {order.id}"
                    )
                    notification.save()
        request.session['cart'] = {}
        return redirect('orders')

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        try:
            # Fetch items from the cart or get relevant product information
            # Replace this logic with your own to fetch items from the cart or database
            line_items = [
                {
                    'price': '{{PRICE_ID}}',  # Replace with the actual price ID
                    'quantity': 1,
                },
            ]

            # Create a new checkout session
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url='http://yourdomain.com/success',  # Replace with your success URL
                cancel_url='http://yourdomain.com/cancel',    # Replace with your cancel URL
            )
        except Exception as e:
            return JsonResponse({'error': str(e)})

        return JsonResponse({'id': checkout_session.id})