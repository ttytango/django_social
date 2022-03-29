from django.views.generic import CreateView

from ..models import FriendRequest, Profile


class FriendRequestCreateView(CreateView):
    model = FriendRequest
    template_name="user/profile/request_friend.html"

    def post(self, request, *args, **kwargs):
        from_user = request.user
        print(request.user)
        to_user = Profile.objects.get(id=6)
        friend_request, created = FriendRequest.objects.get_or_create(
            from_user=from_user,
            to_user=to_user)

        return super().post(request, *args, **kwargs)
    # TODO: continue here