from django.urls import path, include
from django.contrib.auth import views as auth_views
from ..views import (
    CreateAccountView,
    IndexView,

)
urlpatterns = [
    path('register/', CreateAccountView.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', IndexView.as_view(), name="index"),
]