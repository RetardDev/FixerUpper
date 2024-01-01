from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.userprofile import UserProfile
from django.views import View
from store.models.service import Services
from store.models.order import Order
from store.middlewares.auth import auth_middleware

class OrderView(View):
    def get(self, request):
        user_id = request.session.get('user')

        # try:
        #     user_id = UserProfile.objects.get(user_id=user_id)
        # except UserProfile.DoesNotExist:
        #     return redirect('/')


        orders = Order.get_order_by_User(user_id)
        print(orders)
        return render(request, 'order.html', {'orders' : orders})
