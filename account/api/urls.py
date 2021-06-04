from django.urls import path
from account.api.views import (
    registration_view,
    get_user_info,
    logout
)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('register/', registration_view, name="register"),
    path('login/', obtain_auth_token, name="login"),
    path('user/', get_user_info, name="user"),
    path('logout/', logout, name="login"),
]
