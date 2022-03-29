from django.views.generic.base import RedirectView


class IndexRedirectView(RedirectView):

    permanent = False
    query_string = True
    pattern_name = 'user:index'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)



