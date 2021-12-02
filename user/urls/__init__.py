from django.contrib.auth import views as auth_views
from django.urls import path

from ..views import (
    CreateAccountView,
    CustomLoginView,
    IndexView,
    ProfileEditView,
    ProfileDetailView,
    ProfileSearchView,
    PostCreateView,
    PostListView,
    PostUpdateView,
)
from ..views.post_create_view import PostCreateView

app_name = 'user'

urlpatterns = [
    path('register/',
         CreateAccountView.as_view(), name="register"),

    path('logout/',
         auth_views.LogoutView.as_view(), name='logout'),

    path('login/',
         CustomLoginView.as_view(), name='login'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name="user/forms/auth_form.html"),
         name="password-reset"),

    path('',
         IndexView.as_view(),
         name="index"),

    path('<int:pk>/edit-profile/',
         ProfileEditView.as_view(),
         name="edit-profile"),

    path('<int:pk>/',
         ProfileDetailView.as_view(),
         name="profile-detail"),

    path('profiles/',
         ProfileSearchView.as_view(),
         name="search-profiles"),

    path('post/create/',
         PostCreateView.as_view(),
         name='create-post'),

    path('<int:pk>/posts/',
         PostListView.as_view(),
         name='post-list'),

    path('post/<int:pk>/edit',
         PostUpdateView.as_view(),
         name='post-detail'),

]