from django.shortcuts import render , redirect , HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from store.models.service import Services
from store.models.category import Category
from store.models.review import Reviews 
from django.views import View

class Index(View):
     def get(self, request):
        categories = Category.get_all_categories()[:3]
        
        
        reviews = Reviews.objects.select_related('service').all()[:3]
       

        return  render(request, 'index.html', {'categories': categories, 'latest_services': reviews })

    #  def post(self, request):
    #   service = request.POST.get('service')
    #   remove = request.POST.get('remove')
    #   cart = request.session.get('cart')
    #   if cart:
    #     quantity = cart.get(service)
    #     if quantity:
    #       if remove:
    #         if quantity<=1:
    #             cart.pop(service)
    #         else:
    #             cart[service] = quantity-1
    #       else:
    #           cart[service] = service+1

    #     else:
    #         cart[service] = 1
    #   else:
    #      cart = {}
    #      cart[service] = 1

    #   request.session['cart'] = cart
    #   print('cart', request.session['cart'])
    #   return redirect('homepage')


    #   def get(self, request):
    #     return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
  cart = request.session.get('cart')
  if not cart:
      request.session['cart'] = {}
  services = None
  categories = Category.get_all_categories()
  if categoryID:
      services = Services.get_all_services_by_categoryid(categoryID)
  else:
      services = Services.get_all_services();

  data = {}
  data['services'] = services
  data['categories'] = categories

  print('you are : ', request.session.get('email'))
  return render(request, 'index.html', data) 