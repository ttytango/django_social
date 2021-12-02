from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from ..models import Profile

class FriendListView(ListView):
    template_name = "user/account/friend_list.html"
    model = Profile
    context_object_name = "friends"

    @property
    def get_profile(self):
        current_profile = self.kwargs['pk']
        user = Profile.objects.get(user_id=current_profile)
        return user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _(f"{self.get_profile.first_name}'s Friends")
        context['profile'] = self.get_profile
        context['nothing_here_message'] = "You have no friends"
        return context


    def get_queryset(self):
        user = self.get_profile
        return user.friends.all()
