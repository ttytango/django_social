from django.contrib import admin
from ..models import Profile, Post, PostLikes, FriendRequest, Technology, Expertise
from .AccountAdmin import AccountAdmin


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostLikes)
admin.site.register(FriendRequest)
admin.site.register(Technology)
admin.site.register(Expertise)
