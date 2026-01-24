from django.urls import path
from .views import CreatePost, PostList

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('create/',CreatePost.as_view(), name='create_post'),
]