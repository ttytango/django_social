from django.views.generic import ListView
from django.db.models import Q
from ..models import Profile


class ProfileSearchView(ListView):
    model = Profile
    template_name = "user/account/search_results.html"
    context_object_name = 'search_results'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET['search']
        results = Profile.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        return results
