from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

app_name="home"

urlpatterns = [
    path('', views.home, name="Home"),
    path('about/', views.about, name="about"),
    path('records/', views.records, name="records"),
    path('profile/', views.profile, name="profile"),
    path('profile/<int:profile_id>/', views.edit_profile, name="edit_profile"),
]