from django.shortcuts import render , redirect , HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from store.models.service import Services, ServiceImages
from store.models.category import Category
from store.models.review import Reviews 
from django.views import View
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib import messages

class ServiceSingle(View):
    def post(self, request, id):
      service = request.POST.get('service')
      remove = request.POST.get('remove')
      cart = request.session.get('cart')
      if cart:
        quantity = cart.get(service)
        if quantity:
          if remove:
            if quantity<=1:
                cart.pop(service)
            else:
                cart[service] = quantity-1
          else:
              cart[service] = quantity+1

        else:
            cart[service] = 1
      else:
         cart = {}
         cart[service] = 1

      request.session['cart'] = cart
      print('cart', request.session['cart'])
      return redirect(request.META.get('HTTP_REFERER', '/'))


    def get(self, request, id):
      service = Services.get_service_by_id(id)
      service_image = ServiceImages.objects.filter(service=service)
      return render(request, 'serviceSingle.html', {'service' : service, 'service_image': service_image})




    