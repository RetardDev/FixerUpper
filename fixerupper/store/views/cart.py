import json
import stripe
from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from store.models.userprofile import UserProfile
from django.views import  View
from store.models.service import Services
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from datetime import datetime, timedelta
stripe.api_key = settings.STRIPE_SECRET_KEY

class Cart(View):
    def get(self, request):
        try:
            tomorrow = datetime.now() + timedelta(days=1)
            day_after_tomorrow = datetime.now() + timedelta(days=2)

            tomorrow_str = tomorrow.strftime("%d-%m-%Y")
            day_after_tomorrow_str = day_after_tomorrow.strftime("%d-%m-%Y")

            ids = list(request.session.get('cart').keys())
            services = Services.get_services_by_id(ids)
            print(services)
            return render(request, 'cart.html', {'services': services, 
                                                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY, 
                                                'tomorrow' : tomorrow_str, 
                                                'day_after_tomorrow' : day_after_tomorrow_str})
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'cart.html', {'error_message': error_message})


