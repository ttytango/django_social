from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from ..views import ListProfiles, RetrieveProfile

urlpatterns = [
    path('profiles/', ListProfiles.as_view()),
    path('profiles/<int:pk>/', RetrieveProfile.as_view()),
    # path('api-token-auth/', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
]