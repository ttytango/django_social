from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from django.utils.translation import gettext_lazy as _
from ..models import Post

class PostUpdateView(UpdateView):
    model = Post
    template_name = "user/account/post_update_view.html"
    context_object_name = 'post'
    fields = ()

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_object(self):
        return self.model.objects.get(id=self.kwargs['pk'])

    def form_valid(self, form):
        self.object = self.get_object()
        user_id = self.request.user.id
        post_id = self.kwargs['pk']
        object_exists = self.object.postlikes_set.filter(user_id=user_id, post_id=post_id)
        if not object_exists:
            like = self.object.postlikes_set.create(user_id=user_id, post_id=post_id)
            like.save()
            messages.success(message="Great!", request=self.request)
        else:
            messages.error(message="You have already liked this post", request=self.request)
        return super().form_valid(form)


    def get_success_url(self):
        """Return the url of the object's list view"""
        return reverse_lazy('user:post-list', kwargs={'pk': self.object.user_id})
