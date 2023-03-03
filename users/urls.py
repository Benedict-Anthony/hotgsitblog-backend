from django.urls import path
from .views import LoggedInUser, UserCreateView

urlpatterns = [
    path("auth/", UserCreateView.as_view(), name="create-account"),
    path("profile/", LoggedInUser.as_view(), name="create-account"),
    
]