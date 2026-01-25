from django.urls import path
from .views import CreatePost, PostList, PostDetail,UpdatePost,DeletePost, CreateComment, CommentDelete, UpdateComment

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('create/',CreatePost.as_view(), name='create_post'),
    path('post/<int:pk>/',PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/',UpdatePost.as_view(), name='update_post'),
    path('post/<int:pk>/delete/',DeletePost.as_view(), name='delete_post'),
    path('post/<int:pk>/comment/',CreateComment.as_view(), name='create_comment'),
    path('comment/<int:pk>/edit/',UpdateComment.as_view(), name='update_comment'),
    path('comment/<int:pk>/delete/',CommentDelete.as_view(), name='delete_comment'),
]