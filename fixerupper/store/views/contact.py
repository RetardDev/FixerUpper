from django.shortcuts import render, redirect
from django.views import View

class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')