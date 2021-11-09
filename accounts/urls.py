from django.urls import path
from accounts import views
app_name = "accounts"
urlpatterns = [
    path('', views.users, name="accounts"),
    path('userlogin/', views.userlogin, name="userlogin"),
    path('userlogout/',views.userlogout, name='userlogout'),
    path('user_regi/',views.user_regi, name='user_regi'),
]
