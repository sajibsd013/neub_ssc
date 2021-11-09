from django.shortcuts import render, redirect
from blood_app.forms import Search_donor
from blood_app.models import Blood_donor



# Create your views here.

def blood_app(request):
    return redirect('/')


def search_donors(request):
    data = {}
    if request.method == "POST":
        donors = Search_donor(request.POST)
        data.update({"search_donor":donors})

        if donors.is_valid():
            blood_type = donors.cleaned_data['blood_type']
            district = donors.cleaned_data['district']
            donor_list = Blood_donor.objects.filter(
                blood_type=blood_type, district=district
            )
            data.update({"list":donor_list})
            return render(request, 'blood/search_donor.html', context=data)

    return redirect('/')

def donor_profile(request, donor_id):
    donor= Blood_donor.objects.get(pk=donor_id)


    diction= {
        "data": donor
    }
    return render(request, "blood/donor_profile.html", context=diction)