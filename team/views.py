from django.shortcuts import render,redirect
from team.models import Committee_list, Team


# Create your views here.

def team(request):
    c_list = Committee_list.objects.all()
    sorted_committee = sorted(c_list, key = lambda x: x.id, reverse=True)

    data = {
        "sorted_committee": sorted_committee,
    }


    return render(request, 'team/team.html', context= data)


