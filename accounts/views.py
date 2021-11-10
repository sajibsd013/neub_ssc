from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blood_app.models import Blood_donor
from django.contrib.auth import authenticate, logout, login
from accounts.forms import user_rei_form, Sign_in
from django.contrib import messages
# Create your views here.


def users(request):
    return redirect('/')

def userlogin(request):
    if request.method == "POST":
        new_login = Sign_in(request.POST)
        if new_login.is_valid():
            email = new_login.cleaned_data['email']
            date_of_birth = new_login.cleaned_data['date_of_birth']
            password = "Fixed@Pass001"

            if Blood_donor.objects.filter(email=email, date_of_birth=date_of_birth).exists():
                user = authenticate(username=email, password=password)
                if user is not None:
                    # A backend authenticated the credentials
                    login(request, user)
                    return redirect('/')

            else:
                # No backend authenticated the
                messages.warning(request, "Username and Birthday not matched!")
    return render(request, 'forms/login.html')


def userlogout(request):
    logout(request)
    return redirect('/')


def user_regi(request):
    dic = {}
    if request.method == "POST":
        new_user = user_rei_form(request.POST)
        email = request.POST['email']
        password = "Fixed@Pass001"
        phone = request.POST['phone']
        name = request.POST['name']
        dic.update({"blood_donor_form": new_user})

        if User.objects.filter(username=email).exists():
            messages.warning(request, "Email Already exist!")
        elif Blood_donor.objects.filter(phone=phone).exists():
            messages.warning(request, "Number Already exist!")
        elif new_user.is_valid():
            new_user.save(commit=True)
            user = User.objects.create_user(email, email, password)
            user.first_name = name
            user.save()
            messages.success(request, "Regitration Success")
            return render(request, 'forms/login.html')

    return render(request, 'forms/signup_sec.html', context=dic)
