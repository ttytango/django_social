from django.contrib.auth import views as auth_views
from django.urls import path

from ..views import (
    CreateAccountView,
    IndexView,
    ProfileEditView,
)

urlpatterns = [
    path('register/', CreateAccountView.as_view(), name="register"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', IndexView.as_view(), name="index"),
    path('<int:pk>/edit-profile/', ProfileEditView.as_view(), name="edit-profile"),
]