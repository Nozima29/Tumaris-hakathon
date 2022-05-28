from django.contrib.auth import authenticate
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from customers.models import Customer

# Create your views here.


def register(request):
    if request.POST:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        passwd = request.POST.get('password')

        user = User.objects.create(username=firstname)
        user.set_password(passwd)
        user.save()
        customer = Customer.objects.create(
            user=user,
            first_name=firstname,
            last_name=lastname,
            gender=gender,
            age=age
        )
        if email:
            customer.email = email
            customer.save()
        if phone:
            customer.phone = phone
            customer.save()

    return render(request, template_name='pages/register.html')


def login(request):
    if request.POST:
        firstname = request.POST.get('firstname')
        passwd = request.POST.get('password')
        user = authenticate(username=firstname, password=passwd)
        if user:
            return redirect('home')
        return redirect('register')
