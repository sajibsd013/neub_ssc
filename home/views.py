from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blood_app.models import Blood_donor
from accounts.forms import user_rei_form
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'about/about_sec.html')


def records(request):
    return render(request, 'records/records.html')


def profile(request):

    profileData = {
        "datalist": Blood_donor.objects.filter(email=request.user.email),
    }
    return render(request, 'profile/profile.html', context=profileData)


def edit_profile(request,profile_id):
    profile_data = Blood_donor.objects.get(pk=profile_id)
    edit_form = user_rei_form(instance=profile_data)
    profileData = {
        "datalist": Blood_donor.objects.get(pk=profile_id),
        "blood_donor_form":edit_form
    }
    if request.method =="POST":
        edit_form = user_rei_form(request.POST,instance=profile_data)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            messages.success(request, "Profile Edited Successfully")
            return redirect('/profile') 
        
    return render(request, 'profile/edit_profile.html', context=profileData)
