from django.views import View
from django.shortcuts import render, redirect
from store.models.provider import Provider

class About(View):
    def get(self, request):

        
        providers_with_logo = Provider.objects.exclude(provider_logo__isnull=True).exclude(provider_logo='').order_by('pk')[:9]

        # logos = [provider.provider_logo.url for provider in providers_with_logo]
        print(providers_with_logo)

        return render(request, 'about.html', {"providers_with_logo" : providers_with_logo})