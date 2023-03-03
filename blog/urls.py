from django.urls import path
from .views import PostView, PostMutateView


urlpatterns = [
    # post views
    path("", PostView.as_view(), name="posts"),
    path("detail/<slug:slug>/", PostView.as_view(), name="post-detail"),
    
    # create, update, delete view
    
    path("create/", PostMutateView.as_view(), name="create-post"),
    path("admin/", PostMutateView.as_view(), name="mutate"),
    path("mutate/<int:id>/", PostMutateView.as_view(), name="mutate")
]