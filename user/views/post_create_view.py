from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
from ..models import Post
from ..forms import PostCreateForm

class PostCreateView(CreateView):
    template_name = 'user/forms/create_post_form.html'
    model = Post
    form_class = PostCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _("Create Post")
        context['form_title'] = _("Create a Post")
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.user = self.request.user
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user:profile-detail', kwargs={'pk': self.request.user.id})
