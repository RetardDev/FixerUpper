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

class ServiceView(View):
    def get(self, request):
      parent_categories = Category.get_parent_categories()
      services = Services.get_all_services()
      return render(request, 'service.html', {'parent_categories': parent_categories, 'services' : services})

def servicesCategory(request, foo):
      print("Before: " + foo)
      foo = foo.replace('%20', ' ')
      print("After: " + foo)
      try:
            parent_categories = Category.get_parent_categories()
            category = Category.objects.get(name=foo)
         
            services = Services.get_all_services_by_categoryid(category)
            return render(request, 'service.html', {'parent_categories' : parent_categories, 'services' : services})
      except:
            messages.success(request, ("not "))
            return redirect('service')
# def serviceSingle(request, id):
#       service = Services.get_service_by_id(id)
#       service_image = ServiceImages.objects.filter(service=service)
#       return render(request, 'serviceSingle.html', {'service' : service, 'service_image': service_image})