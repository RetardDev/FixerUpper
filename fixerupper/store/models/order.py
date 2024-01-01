from django.db import models
from .service  import Services
from .userprofile import UserProfile
import datetime

class Order(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_order_by_User(user_id):
        return Order.objects.filter(user=UserProfile.objects.get(user_id=user_id)).order_by('-date')

class Notification(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    provider = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Notification: {self.message}"