from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10)
    is_provider = models.BooleanField(default=False)

    def register(self):
        self.save()


    @staticmethod
    def get_profile_by_email(email):
        try:
            return UserProfile.objects.get(email=email).user
        except:
            return False

    def isExists(self):
        if UserProfile.objects.filter(email = self.email):
            return True
        return False


    def __str__(self):
        return f"Username: {self.user.username}, Email: {self.email}"