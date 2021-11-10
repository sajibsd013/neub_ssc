from accounts.forms import Sign_in, user_rei_form
from team.models import Team, Committee_list
from blood_app.models import Blood_donor
from blood_app.forms import Search_donor

def add_var_to_context(request):
    sign_in = Sign_in()
    search_donor = Search_donor()
    blood_donor_form = user_rei_form()
    current_committee = Committee_list.objects.all().filter(active=True)
    team = Team.objects.all()
    donor = Blood_donor.objects.all()


    return{
        "login_form": sign_in,
        "members" : team,
        "blood_donor_form": blood_donor_form,
        "current_committee": current_committee,
        "list": donor,
        "search_donor": search_donor,
    }