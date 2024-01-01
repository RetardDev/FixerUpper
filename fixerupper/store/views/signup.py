from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from store.models.userprofile import UserProfile
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        username = request.POST.get('username')
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'phone': phone,
            'email' : email
        }
        error_message = None
       
        error_message = self.validateCustomer(first_name, last_name, phone, email, password)

        if not error_message:
            # password = make_password(password) 
            user = User.objects.create_user(username=username, email=email, password=password,
                                            first_name=first_name, last_name=last_name)
            user_profile = UserProfile.objects.create(user=user, phone=phone)
            
            # customer.password = make_password(customer.password)
            # customer.register()
            return redirect('/admin/')
        else:
            data = {
                'error': error_message,
                'value': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, first_name, last_name, phone, email, password):
        error_message = None
        if not first_name:
            error_message = "Please Enter your First Name !!"
        elif len(first_name) < 3:
            error_message = "First Name must be 3 characters or longer"
        elif not last_name:
            error_message = "Please Enter your Last Name"
        elif len(last_name) < 3:
            error_message = "Last Name must be 3 characters or longer"
        elif not phone:
            error_message = "Please Enter your phone number"
        elif len(phone) < 10:
            error_message = "Phone Number must be 10 characters long"
        elif not email:
            error_message = "Please Enter your email"
        elif len(email) < 5:
            error_message = "Email must be 5 characters or longer"
        elif not password:
            error_message = "Please Enter your password"
        elif len(password) < 5:
            error_message = "Password must be 5 characters or longer"
        return error_message

