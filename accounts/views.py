from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blood_app.models import Blood_donor
from django.contrib.auth import authenticate, logout, login
from accounts.forms import user_rei_form, Sign_in, Sing_up
from django.contrib import messages
# Create your views here.


def users(request):
    return redirect('/')


def userlogin(request):
    if request.method == "POST":
        new_login = Sign_in(request.POST)
        if new_login.is_valid():
            username = new_login.cleaned_data['username']
            password = new_login.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect('/')

            else:
                # No backend authenticated the
                messages.warning(request, "Username and password not matched!")
    return render(request, 'forms/login.html')


def userlogout(request):
    logout(request)
    return redirect('/')


def user_regi(request):
    dic = {}
    if request.method == "POST":

        new_user = user_rei_form(request.POST)
        new_user_s = Sing_up(request.POST)
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = request.POST['username']
        phone = request.POST['phone']
        name = request.POST['name']
        dic.update({"blood_donor_form": new_user, "signup_form": new_user_s})
        print(username)

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username not avilable!")
        elif User.objects.filter(email=email).exists():
            messages.warning(request, "Email Already exist!")
        elif Blood_donor.objects.filter(phone=phone).exists():
            messages.warning(request, "Number Already exist!")
        elif password1 != password2:
            messages.warning(request, "Password not matched!")
        elif len(password1) < 8:
            messages.warning(request, "Password to short!")
        elif new_user.is_valid():
            new_user.save(commit=True)
            user = User.objects.create_user(username, email, password1)
            user.first_name = name
            user.save()
            messages.success(request, "Regitration Success")
            return render(request, 'forms/login.html')

    return render(request, 'forms/signup_sec.html', context=dic)
