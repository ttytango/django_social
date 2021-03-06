from django.views.generic import ListView
from ..models import Post, Profile

class PostListView(ListView):
    """List view to show posts from users by url pk"""
    template_name = 'user/posts/post_list_view.html'
    context_object_name = 'posts'
    model = Post
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(id=self.kwargs['pk'])
        context['nothing_here_message'] = f"This user has not published any {self.context_object_name} yet"
        return context

    def get_queryset(self):
        qs = Post.objects.filter(user_id=self.kwargs['pk']).order_by('-date_time_created')
        return qs

