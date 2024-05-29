from django.contrib import admin
from django.urls import path
from .views import register_user, user_logout,LoginWithOTP, ValidateOTP,login_with_face

urlpatterns = [
    path('register/', register_user, name='register'),
    path('logout/', user_logout, name='logout'),
    path('login-with-otp/', LoginWithOTP.as_view(), name='login-with-otp'),
    path('validate-otp/', ValidateOTP.as_view(), name='validate-otp'),
    path('login/face/', login_with_face, name='login_with_face'),
    
]
