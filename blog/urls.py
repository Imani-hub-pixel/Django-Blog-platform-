from django.urls import path
from .views import CreatePost, PostList, PostDetail

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('create/',CreatePost.as_view(), name='create_post'),
    path('post/<int:pk>/',PostDetail.as_view(), name='post_detail'),
]