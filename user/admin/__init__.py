from django.contrib import admin
from ..models import Profile
from .AccountAdmin import AccountAdmin


admin.site.register(Profile)