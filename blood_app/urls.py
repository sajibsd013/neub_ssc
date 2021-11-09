from django.urls import path
from blood_app import views


app_name="blood_app"


urlpatterns = [
    path('', views.blood_app, name="blood_app"),
    path('search_donors/', views.search_donors, name="search_donors"),
    path('donor/<int:donor_id>/', views.donor_profile, name="donor_profile"),
]
