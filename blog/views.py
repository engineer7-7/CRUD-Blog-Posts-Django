from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

# Create your views here.
""" Function Views"""

# grab all posts
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/home.html', context={
#         'posts': posts
#     })
#
#
# # select one specific post
# def post_detail(request, post_id):
#     post = get_object_or_404(Post, id=post_id)  # this is like SELECT * FROM TABLE WHERE ID =?
#     return render(request, 'blog/post_detail.html', context={
#         'post': post
#     })
"""Class Views"""


# read all posts
class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


# read specific post
class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# post a new post
class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = [
        'title', 'author', 'body'
    ]


# update view
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = [
        'title', 'body'
    ]


# delete view
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
