from django.contrib import admin
from .models.category import Category
from .models.userprofile import UserProfile
from .models.provider import Provider
from .models.service import Services, ServiceImages
from .models.review import Reviews
from .models.order import Order, Notification
# # Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class AdminReviews(admin.ModelAdmin):
    list_display = ['client', 'service', 'provider', 'rating', 'comment']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Services, AdminProduct)
admin.site.register(ServiceImages)
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Reviews, AdminReviews)
admin.site.register(Notification)
admin.site.register(Provider)