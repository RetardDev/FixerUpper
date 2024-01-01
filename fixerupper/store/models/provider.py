from django.db import models
from .userprofile import UserProfile

class Provider(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    services_offered = models.ManyToManyField('Services')
    provider_logo = models.ImageField(upload_to='images/provider-logo', null=True)

    def __str__(self):
        if self.user_profile and self.user_profile.user:
            return self.user_profile.user.username
        return "No username available"