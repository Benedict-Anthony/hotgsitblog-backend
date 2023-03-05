from django.urls import path
from .views import PostView, PostMutateView


urlpatterns = [
    # post views
    path("", PostView.as_view(), name="posts"),
    path("detail/<slug:slug>/", PostView.as_view(), name="post-detail"),
    
    # create, update, delete and patch view
    
    path("admin/", PostMutateView.as_view(), name="admin"),
    path("admin/mutate/", PostMutateView.as_view(), name="mutate"),
    path("admin/mutate/<int:id>/", PostMutateView.as_view(), name="mutate")
]