from django.contrib import admin
from ..models import Profile, Post, PostLikes
from .AccountAdmin import AccountAdmin


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostLikes)
