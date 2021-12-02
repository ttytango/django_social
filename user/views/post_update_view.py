from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
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
        print(self.request.POST)
        self.object = self.get_object()
        user_id = self.request.user.id
        post_id = self.kwargs['pk']
        object_exists = self.object.postlikes_set.filter(user_id=user_id, post_id=post_id)
        if not object_exists:
            like = self.object.postlikes_set.create(user_id=user_id, post_id=post_id)
            like.save()
        return HttpResponse(self.object.postlikes_set.count())
