from django.contrib import admin
from django.urls import path 
from .views.home import Index
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut, CreateCheckoutSessionView
from .views.contact import Contact

from .views.services import ServiceView, servicesCategory, serviceSingle
from .views.serviceSin import ServiceSingle
from .views.orders import OrderView
from .views.about import About
from .views.error import error
from .middlewares.auth import auth_middleware
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    
    path('error', error, name='error'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('contact', Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    path('cart', auth_middleware(Cart.as_view()), name='cart'),
    path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('service', ServiceView.as_view(), name='service'),
    path('category/<str:foo>', servicesCategory, name='servicesCategory'),
    path('service/<int:id>', ServiceSingle.as_view(), name='serviceSingle'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)