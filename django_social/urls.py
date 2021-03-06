"""django_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import IndexRedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user.urls')),
    path('', IndexRedirectView.as_view(), name='homepage'),
    path('password-reset/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user/forms/auth_form.html"), name="password_reset_confirm"),
    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="user/registration/password_reset_complete.html"), name="password_reset_complete"),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="user/registration/password_reset_done.html"), name='password_reset_done'),

    # API views
    path('api/v1/api-auth/', include('rest_framework.urls')),
    path('api/v1/', include('user.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)