from django.db import models
from .category import Category
from .provider import Provider

class Services(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null= True)
    image = models.ImageField(upload_to='images/services', null=True)
    providers = models.ManyToManyField(Provider, related_name='provided_services', blank=True)

    @staticmethod
    def get_services_by_id(ids):
        return Services.objects.filter(id__in=ids)
    @staticmethod
    def get_all_services():
        return Services.objects.all()

    @staticmethod
    def get_all_services_by_categoryid(category_id):
        if category_id:
            return Services.objects.filter(category=category_id)
        else:
            return Services.get_all_services();

    @staticmethod
    def get_all_services_by_category_name(category_name):
        if category_name:
            try: 
                category = Category.objects.get(name=category_name)
                return Services.objects.filter(category=category)
            except Category.DoesNotExist:
                return Services.objects.none()
            else:
                return Services.get_all_services()

    @staticmethod
    def get_service_by_id(service_id):
        try:
            return Services.objects.get(pk=service_id)
        except Services.DoesNotExist:
            return None

    def __str__(self):
        return self.name

class ServiceImages(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/services/', null=True)

    def __str__(self):
        return f"Image for {self.service.name}"