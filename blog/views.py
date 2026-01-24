from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment

# Create your views here.
class CreatePost(CreateView):
    model=Post 
    fields='__all__'
    template_name='blog/post_form.html'
    success_url=reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostList(ListView):
    model=Post
    template_name='blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return super().get_queryset().order_by('-created_at')


class PostDetail(DetailView):
    model=Post
    template_name='blog/post_detail.html'
    context_object_name = 'post'

class UpdatePost(UpdateView):
    model=Post
    fields='__all__'
    template_name='blog/post_form.html'
    success_url=reverse_lazy('post_list')

class DeletePost(DeleteView):
    model=Post
    template_name='blog/delete_post.html'
    success_url=reverse_lazy('post_list')