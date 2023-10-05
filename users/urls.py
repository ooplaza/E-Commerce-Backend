from django.urls import path
from . views import (
    CustomUserRegister,
    CustomUserLogout,
    CustomUserProfile
)

urlpatterns = [
    path('info', CustomUserProfile.as_view(), name='User_Info'),
    path('register', CustomUserRegister.as_view(), name='Register_User'),
    path('logout/blacklist', CustomUserLogout.as_view(), name='Logout_User'),
]