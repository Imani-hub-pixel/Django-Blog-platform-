from django.urls import path
from .views import CreatePost, PostList, PostDetail,UpdatePost,DeletePost

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('create/',CreatePost.as_view(), name='create_post'),
    path('post/<int:pk>/',PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete/',DeletePost.as_view(), name='delete_post'),
]